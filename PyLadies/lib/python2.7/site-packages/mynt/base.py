# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Parser(object):
    accepts = ()
    
    
    def __init__(self, options = None):
        self.options = options if options is not None else {}
        
        self.setup()
    
    
    def parse(self, content):
        raise NotImplementedError('A parser must implement parse.')
    
    def setup(self):
        pass

class Renderer(object):
    def __init__(self, path, options = None, globals_ = None):
        self.path = path
        self.options = options if options is not None else {}
        self.globals = globals_ if globals_ is not None else {}
        
        self.setup()
    
    
    def from_string(self, string, data = None):
        raise NotImplementedError('A renderer must implement from_string.')
    
    def register(self, key, value):
        raise NotImplementedError('A renderer must implement register.')
    
    def render(self, template, data = None):
        raise NotImplementedError('A renderer must implement render.')
    
    def setup(self):
        pass
