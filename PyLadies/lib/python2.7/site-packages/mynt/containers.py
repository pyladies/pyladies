# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import OrderedDict
from datetime import datetime

import yaml

from mynt.exceptions import ConfigException
from mynt.fs import Directory
from mynt.utils import get_logger, normpath, Url


yaml.add_constructor('tag:yaml.org,2002:str', lambda loader, node: loader.construct_scalar(node))

logger = get_logger('mynt')


class Config(dict):
    def __init__(self, string):
        super(Config, self).__init__()
        
        try:
            self.update(yaml.load(string))
        except yaml.YAMLError:
            raise ConfigException('Config contains unsupported YAML.')
        except:
            logger.debug('..  config file is empty')
            
            pass

class Data(object):
    def __init__(self, items, archives, tags):
        self.items = items
        self.archives = archives
        self.tags = tags
    
    
    def __iter__(self):
        return self.items.__iter__()

class Item(dict):
    def __init__(self, src, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        
        self.__src = src
    
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.__src

class Tag(object):
    def __init__(self, name, url, count, items, archives):
        self.name = name
        self.url = url
        self.count = count
        self.items = items
        self.archives = archives
    
    
    def __iter__(self):
        return self.items.__iter__()


class Container(object):
    def __init__(self, name, src, config):
        self._pages = None
        
        self.name = name
        self.path = src
        self.config = {} if config is None else config
        self.data = Data([], OrderedDict(), OrderedDict())
    
    
    def _get_pages(self):
        pages = []
        
        for item in self.items:
            if item['layout'] is None:
                continue
            
            pages.append((item['layout'], {'item': item}, item['url']))
        
        return pages
    
    
    def add(self, item):
        self.items.append(item)
    
    def archive(self):
        pass
    
    def sort(self):
        pass
    
    def tag(self):
        pass
    
    
    @property
    def archives(self):
        return self.data.archives
    
    @property
    def items(self):
        return self.data.items
    
    @property
    def pages(self):
        if self._pages is None:
            self._pages = self._get_pages()
        
        return self._pages
    
    @property
    def tags(self):
        return self.data.tags


class Items(Container):
    _sort_order = {
        'asc': False,
        'desc': True
    }
    
    
    def __init__(self, name, src, config):
        super(Items, self).__init__(name, src, config)
        
        self.path = Directory(normpath(src.path, '_containers', self.name))
    
    
    def _archive(self, items, archive):
        for item in items:
            year, month = datetime.utcfromtimestamp(item['timestamp']).strftime('%Y %B').decode('utf-8').split()
            
            if year not in archive:
                archive[year] = {
                    'months': OrderedDict({month: [item]}),
                    'url': Url.from_format(self.config['archives_url'], year),
                    'year': year
                }
            elif month not in archive[year]['months']:
                archive[year]['months'][month] = [item]
            else:
                archive[year]['months'][month].append(item)
    
    def _get_pages(self):
        pages = super(Items, self)._get_pages()
        
        if self.config['archive_layout'] and self.archives:
            for archive in self.archives.itervalues():
                pages.append((
                    self.config['archive_layout'],
                    {'archive': archive},
                    archive['url']
                ))
        
        if self.config['tag_layout'] and self.tags:
            for tag in self.tags.itervalues():
                pages.append((
                    self.config['tag_layout'],
                    {'tag': tag},
                    tag.url
                ))
        
        return pages
    
    def _relate(self):
        for i, item in enumerate(self.items):
            if i:
                item['prev'] = self.items[i - 1]
            else:
                item['prev'] = None
            
            try:
                item['next'] = self.items[i + 1]
            except IndexError:
                item['next'] = None
    
    def _sort(self, container, key, order = 'asc'):
        reverse = self._sort_order.get(order.lower(), False)
        
        def sort(item):
            try:
                attribute = item.get(key, item)
            except AttributeError:
                attribute = getattr(item, key, item)
            
            if isinstance(attribute, basestring):
                return attribute.lower()
            
            return attribute
        
        container.sort(key = sort, reverse = reverse)
    
    
    def archive(self):
        self._archive(self.items, self.archives)
        
        for tag in self.tags.itervalues():
            self._archive(tag.items, tag.archives)
    
    def sort(self):
        self._sort(self.items, self.config['sort'], self.config['order'])
        self._relate()
    
    def tag(self):
        tags = []
        
        for item in self.items:
            item['tags'].sort(key = unicode.lower)
            
            for tag in item['tags']:
                if tag not in self.tags:
                    self.tags[tag] = []
                
                self.tags[tag].append(item)
        
        for name, items in self.tags.iteritems():
            tags.append(Tag(
                name,
                Url.from_format(self.config['tags_url'], name),
                len(items),
                items,
                OrderedDict()
            ))
        
        self._sort(tags, 'name')
        self._sort(tags, 'count', 'desc')
        
        self.tags.clear()
        
        for tag in tags:
            self.tags[tag.name] = tag


class Posts(Items):
    def __init__(self, src, site):
        super(Posts, self).__init__('posts', src, self._get_config(site))
        
        self.path = Directory(normpath(src.path, '_posts'))
    
    
    def _get_config(self, site):
        config = {
            'archives_url': 'archives_url',
            'archive_layout': 'archive_layout',
            'order': 'posts_order',
            'sort': 'posts_sort',
            'tags_url': 'tags_url',
            'tag_layout': 'tag_layout',
            'url': 'posts_url'
        }
        
        for k, v in config.iteritems():
            config[k] = site.get(v)
        
        return config
