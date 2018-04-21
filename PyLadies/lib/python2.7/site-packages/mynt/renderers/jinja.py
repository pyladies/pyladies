# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import OrderedDict
from datetime import datetime
import gettext
import locale
from os import path as op
from re import sub

from jinja2 import Environment, FileSystemLoader, PrefixLoader
from jinja2.exceptions import TemplateNotFound

from mynt.base import Renderer as _Renderer
from mynt.exceptions import RendererException
from mynt.utils import normpath, Url


class _PrefixLoader(PrefixLoader):
    def get_loader(self, template):
        try:
            if not self.delimiter:
                for prefix in self.mapping:
                    if template.startswith(prefix):
                        name = template.replace(prefix, '', 1)
                        loader = self.mapping[prefix]
                        
                        break
                else:
                    raise TemplateNotFound(template)
            else:
                prefix, name = template.split(self.delimiter, 1)
                loader = self.mapping[prefix]
        except (KeyError, ValueError):
            raise TemplateNotFound(template)
        
        # Gross hack to appease Jinja when handling Windows paths.
        if op.sep != '/':
            name = name.replace(op.sep, '/')
        
        return loader, name


class Renderer(_Renderer):
    config = {}
    
    
    def _absolutize(self, html):
        def _replace(match):
            return self._get_url(match.group(1).replace(self.globals['site']['base_url'], '', 1), True)
        
        return sub(r'(?<==")({0}[^"]*)'.format(self.globals['site']['base_url']), _replace, html)
    
    def _date(self, ts, format = '%A, %B %d, %Y'):
        if ts is None:
            return datetime.utcnow().strftime(format).decode('utf-8')
        
        return datetime.utcfromtimestamp(ts).strftime(format).decode('utf-8')
    
    def _get_asset(self, asset):
        return Url.join(self.globals['site']['base_url'], self.globals['site']['assets_url'], asset)
    
    def _get_url(self, url = '', absolute = False):
        parts = [self.globals['site']['base_url'], url]
        domain = self.globals['site']['domain']
        
        if absolute and domain:
            if not domain.startswith(('http://', 'https://')):
                domain = 'http://' + domain
            
            parts.insert(0, domain)
        
        return Url.join(*parts)
    
    def _items(self, dict_):
        return dict_.iteritems()
    
    def _values(self, dict_):
        return dict_.itervalues()
    
    
    def from_string(self, string, data = None):
        if data is None:
            data = {}
        
        template = self.environment.from_string(string)
        
        return template.render(**data)
    
    def register(self, data):
        self.globals.update(data)
        self.environment.globals.update(data)
    
    def render(self, template, data = None):
        if data is None:
            data = {}
        
        try:
            template = self.environment.get_template(template)
        except TemplateNotFound:
            raise RendererException('Template not found.')
        
        return template.render(**data)
    
    def setup(self):
        self.config.update(self.options)
        self.config['loader'] = _PrefixLoader(OrderedDict([
            (op.sep, FileSystemLoader(self.path)),
            ('', FileSystemLoader(normpath(self.path, '_templates')))
        ]), None)
        
        self.environment = Environment(**self.config)
        
        self.environment.filters['absolutize'] = self._absolutize
        self.environment.filters['date'] = self._date
        self.environment.filters['items'] = self._items
        self.environment.filters['values'] = self._values
        
        self.environment.globals.update(self.globals)
        self.environment.globals['get_asset'] = self._get_asset
        self.environment.globals['get_url'] = self._get_url
        
        if 'extensions' in self.config and 'jinja2.ext.i18n' in self.config['extensions']:
            try:
                langs = [locale.getlocale(locale.LC_MESSAGES)[0].decode('utf-8')]
            except AttributeError:
                langs = None
            
            self.environment.install_gettext_translations(gettext.translation(gettext.textdomain(), normpath(self.path, '_locales'), langs, fallback = True))
