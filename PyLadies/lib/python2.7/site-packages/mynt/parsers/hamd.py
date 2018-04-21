# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from collections import OrderedDict
from copy import deepcopy
import re
from textwrap import dedent

from mynt.base import Parser as _Parser


class Parser(_Parser):
    accepts = ('.hamd',)
    
    
    _BLOCK = re.compile(r'^(\S.+?)(?=(?:$\s+(?:^\S|\Z)|\Z))', re.M | re.S)
    _TAG_INLINE = re.compile(r'%(\S+)=(?: (?<!\\)\{(:|\^) ([^}]+) \})?(?: (.+))?$')
    _TAG_BLOCK = re.compile(r'%(\S+)(?: (?<!\\)\{(:|\^) ([^}]+) \})?$\s+?^((?:\s+^)?(.+?)(?:$\s+)?\Z)', re.M | re.S)
    _VOID = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'menuitem', 'meta', 'param', 'source', 'track', 'wbr']
    _ID = re.compile(r'#([a-z][a-z0-9_:.-]*)$', re.I)
    _CLASS = re.compile(r'\.([a-z][a-z0-9_-]*)$', re.I)
    _ATTRIBUTE = re.compile(r'(\S+?): (\S+)$')
    
    _CODE = re.compile(r'(?:\A|(?<=\W))`(.+?)(?<!\\)`(?=\Z|\W)', re.U)
    _EM = re.compile(r'(?:\A|(?<=\W))(_|\*)(.+?)(?<!\\)\1(?=\Z|\W)', re.U)
    _IMAGE = re.compile(r'')
    _LINK_INLINE = re.compile(r'(?<!\\|!)\[((?<!\\)[^\[\]]+)\]\(((?<!\\)[^)]+)\)')
    _STRONG = re.compile(r'(?:\A|(?<=\W))(__|\*\*)(.+?)(?<!\\)\1(?=\Z|\W)', re.U)
    
    _stack = []
    
    _html = ''
    
    defaults = {}
    
    
    def _build_tag(self, tag, attributes = None, target = -1):
        level = 0
        
        tags = tag.split('>')
        attributes = self._parse_attributes(attributes) if attributes else ''
        target = tags.index(tags[target])
        
        for i, tag in enumerate(tags):
            if tag not in self._VOID:
                level += 1
                
                self._stack.append(tag)
            
            format = '<{0}{1}>' if i == target else '<{0}>'
            
            tags[i] = format.format(tag, attributes)
        
        return (level, ''.join(tags))
    
    def _get_blocks(self, string):
        return self._BLOCK.findall(string)
    
    def _parse_attribute(self, string):
        string = string.strip()
        
        try:
            if string.startswith('#'):
                return ('id', self._ID.match(string).group(1))
            elif string.startswith('.'):
                return ('class', self._CLASS.match(string).group(1))
            else:
                return ('attribute', self._ATTRIBUTE.match(string).groups())
        except AttributeError:
            raise Exception('Invalid attribute.')
    
    def _parse_attributes(self, string):
        attributes = OrderedDict([
            ('id', {
                'format': ' id="{0}"',
                'values': []
            }),
            ('class', {
                'format': ' class="{0}"',
                'values': []
            }),
            ('attribute', {
                'format': ' {0}',
                'values': []
            })
        ])
        
        for type_, value in map(self._parse_attribute, string.split(',')):
            if type_ == 'attribute':
                value = '{0}="{1}"'.format(*value)
            
            attributes[type_]['values'].append(value)
        
        for type_, data in attributes.items():
            value = ' '.join(data['values'])
            
            if value:
                attributes[type_] = data['format'].format(value)
            else:
                del attributes[type_]
        
        return ''.join(attributes.itervalues())
    
    def _parse_inline(self, string):
        string = self._STRONG.sub(r'<strong>\2</strong>', string)
        string = self._EM.sub(r'<em>\2</em>', string)
        string = self._CODE.sub(r'<code>\1</code>', string)
        
        while True:
            last = string
            string = self._LINK_INLINE.sub(r'<a href="\2">\1</a>', string)
            
            if string == last:
                break
        
        return string
    
    def _parse_tag(self, string):
        try:
            tag, target, attributes, content = self._TAG_INLINE.match(string).groups()
            
            if content is None:
                content = ''
        except AttributeError:
            try:
                tag, target, attributes, raw, content = self._TAG_BLOCK.match(string).groups()
                
                if 'pre' in tag or 'pre' in self._stack:
                    content = raw
                
                content = dedent(content)
            except AttributeError:
                raise Exception('Invalid tag.')
        
        target = -1 if target == ':' else 0
        
        return (self._build_tag(tag, attributes, target), content)
    
    
    def _parse(self, hamd):
        for block in self._get_blocks(hamd):
            if block.startswith('%'):
                tags, content = self._parse_tag(block)
                level, tag = tags
                
                self._html += tag
                
                if content.startswith('%'):
                    self._parse(content)
                else:
                    self._html += self._parse_inline(content)
                
                while level:
                    self._html += '</{0}>'.format(self._stack.pop())
                    
                    level -= 1
    
    
    def parse(self, hamd):
        self._html = ''
        
        del self._stack[:]
        
        self._parse(hamd)
        
        return self._html
    
    def setup(self):
        self.config = deepcopy(self.defaults)
        
        for k, v in self.options.iteritems():
            self.config[k].update(v)
