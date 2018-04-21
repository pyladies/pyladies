# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from calendar import timegm
from datetime import datetime
from importlib import import_module
from os import path as op
import re

from pkg_resources import DistributionNotFound, iter_entry_points, load_entry_point
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

from mynt.containers import Config, Container, Item, Items, Posts
from mynt.exceptions import ConfigException, ContentException, ParserException, RendererException
from mynt.fs import File
from mynt.utils import get_logger, normpath, Timer, unescape, Url


logger = get_logger('mynt')


class Reader(object):
    def __init__(self, src, dest, site, writer):
        self._writer = writer
        
        self._parsers = {}
        self._extensions = {}
        self._cache = {}
        
        self.src = src
        self.dest = dest
        self.site = site
        
        self._find_parsers()
    
    
    def _find_parsers(self):
        for parser in iter_entry_points('mynt.parsers'):
            name = parser.name.decode('utf-8')
            
            try:
                Parser = parser.load()
            except DistributionNotFound as e:
                logger.debug('@@ The %s parser could not be loaded due to a missing requirement: %s.', name, unicode(e))
                
                continue
            
            for extension in Parser.accepts:
                if extension in self._extensions:
                    self._extensions[extension].append(name)
                else:
                    self._extensions[extension] = [name]
            
            self._parsers[name] = Parser
        
        for parsers in self._extensions.itervalues():
            parsers.sort(key = unicode.lower)
    
    def _get_date(self, mtime, date):
        if not date:
            return mtime
        
        d = [None, None, None, 0, 0]
        
        for i, v in enumerate(date.split('-')):
            d[i] = v
        
        if not d[3]:
            d[3], d[4] = mtime.strftime('%H %M').decode('utf-8').split()
        elif not d[4]:
            d[4] = '{0:02d}'.format(d[4])
        
        return datetime.strptime('-'.join(d), '%Y-%m-%d-%H-%M')
    
    def _get_parser(self, f, parser = None):
        if not parser:
            try:
                parser = self._extensions[f.extension][0]
            except KeyError:
                raise ParserException('No parser found that accepts \'{0}\' files.'.format(f.extension),
                    'src: {0}'.format(f.path))
        
        if parser in self._cache:
            return self._cache[parser]
        
        options = self.site.get(parser, None)
        
        if parser in self._parsers:
            Parser = self._parsers[parser](options)
        else:
            try:
                Parser = import_module('mynt.parsers.{0}'.format(parser)).Parser(options)
            except ImportError:
                raise ParserException('The {0} parser could not be found.'.format(parser))
        
        self._cache[parser] = Parser
        
        return Parser
    
    def _parse_filename(self, f):
        date, text = re.match(r'(?:(\d{4}(?:-\d{2}-\d{2}){1,2})-)?(.+)', f.name).groups()
        
        return (
            text,
            self._get_date(f.mtime, date)
        )
    
    
    def _parse_container(self, container):
        for f in container.path:
            container.add(self._parse_item(container.config, f))
        
        container.sort()
        container.tag()
        container.archive()
        
        return container
    
    def _parse_item(self, config, f, simple = False):
        Timer.start()
        
        item = Item(f.path)
        
        try:
            frontmatter, bodymatter = re.search(r'\A---\s+^(.+?)$\s+---\s*(.*)\Z', f.content, re.M | re.S).groups()
            frontmatter = Config(frontmatter)
        except AttributeError:
            raise ContentException('Invalid frontmatter.',
                'src: {0}'.format(f.path),
                'frontmatter must not be empty')
        except ConfigException:
            raise ConfigException('Invalid frontmatter.',
                'src: {0}'.format(f.path),
                'fontmatter contains invalid YAML')
        
        if 'layout' not in frontmatter:
            raise ContentException('Invalid frontmatter.',
                'src: {0}'.format(f.path),
                'layout must be set')
        
        frontmatter.pop('url', None)
        
        parser = self._get_parser(f, frontmatter.get('parser', config.get('parser', None)))
        
        text, date = self._parse_filename(f)
        content = parser.parse(self._writer.from_string(bodymatter, frontmatter))
        
        item['content'] = content
        item['date'] = date.strftime(self.site['date_format']).decode('utf-8')
        item['timestamp'] = timegm(date.utctimetuple())
        
        if simple:
            item['url'] = Url.from_path(f.root.path.replace(self.src.path, ''), text)
        else:
            item['excerpt'] = re.search(r'\A.*?(?:<p>(.+?)</p>)?', content, re.M | re.S).group(1)
            item['tags'] = []
            item['url'] = Url.from_format(config['url'], text, date, frontmatter)
        
        item.update(frontmatter)
        
        logger.debug('..  (%.3fs) %s', Timer.stop(), f.path.replace(self.src.path, ''))
        
        return item
    
    
    def parse(self):
        posts = self._parse_container(Posts(self.src, self.site))
        containers = {}
        miscellany = Container('miscellany', self.src, None)
        pages = posts.pages
        
        for name, config in self.site['containers'].iteritems():
            container = self._parse_container(Items(name, self.src, config))
            
            containers[name] = container
            pages.extend(container.pages)
        
        for f in miscellany.path:
            if f.extension in self._extensions:
                miscellany.add(self._parse_item(miscellany.config, f, True))
            elif f.extension in ('.html', '.htm', '.xml'):
                pages.append((f.path.replace(self.src.path, ''), None, None))
        
        pages.extend(miscellany.pages)
        
        return (posts, containers, pages)

class Writer(object):
    def __init__(self, src, dest, site):
        self.src = src
        self.dest = dest
        self.site = site
        
        self._renderer = self._get_renderer()
    
    
    def _get_path(self, url):
        parts = [self.dest.path] + url.split('/')
        
        if url.endswith('/'):
            parts.append('index.html')
        
        path = normpath(*parts)
        
        if op.commonprefix((self.dest.path, path)) != self.dest.path:
            raise ConfigException('Invalid URL.',
                'url: {0}'.format(url),
                'path traversal is not allowed')
        
        return path
    
    def _get_renderer(self):
        renderer = self.site['renderer']
        options = self.site.get(renderer, None)
        
        try:
            Renderer = load_entry_point('mynt', 'mynt.renderers', renderer)
        except DistributionNotFound as e:
            raise RendererException('The {0} renderer requires {1}.'.format(renderer, unicode(e)))
        except ImportError:
            try:
                Renderer = import_module('mynt.renderers.{0}'.format(renderer)).Renderer
            except ImportError:
                raise RendererException('The {0} renderer could not be found.'.format(renderer))
        
        return Renderer(self.src.path, options)
    
    def _highlight(self, match):
        language, code = match.groups()
        formatter = HtmlFormatter(linenos = 'table')
        code = unescape(code)
        
        try:
            code = highlight(code, get_lexer_by_name(language), formatter)
        except ClassNotFound:
            code = highlight(code, get_lexer_by_name('text'), formatter)
        
        return '<div class="code"><div>{0}</div></div>'.format(code)
    
    def _pygmentize(self, html):
        return re.sub(r'<pre><code[^>]+data-lang="([^>]+)"[^>]*>(.+?)</code></pre>', self._highlight, html, flags = re.S)
    
    
    def from_string(self, string, data = None):
        return self._renderer.from_string(string, data)
    
    def register(self, data):
        self._renderer.register(data)
    
    def render(self, template, data = None, url = None):
        url = url if url is not None else template
        path = self._get_path(url)
        
        try:
            Timer.start()
            
            content = self._renderer.render(template, data)
            
            if self.site['pygmentize']:
                content = self._pygmentize(content)
            
            logger.debug('..  (%.3fs) %s', Timer.stop(), path.replace(self.dest.path, ''))
        except RendererException as e:
            raise RendererException(e.message,
                '{0} in container item {1}'.format(template, data.get('item', url)))
        
        return File(path, content)
