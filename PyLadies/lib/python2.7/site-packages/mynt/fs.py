# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from codecs import open
from datetime import datetime
from os import makedirs, path as op, remove, walk
from re import search
import shutil
from sys import exc_info
import traceback

from watchdog.events import FileSystemEventHandler

from mynt.exceptions import FileSystemException
from mynt.utils import abspath, get_logger, normpath, Timer


logger = get_logger('mynt')


class Directory(object):
    def __init__(self, path):
        self.path = abspath(path)
        
        if self.is_root:
            raise FileSystemException('Root is not an acceptible directory.')
    
    
    def _ignored(self, path, names):
        return [name for name in names if name.startswith(('.', '_'))]
    
    
    def cp(self, dest, ignore = True):
        if self.exists:
            dest = Directory(dest)
            ignore = self._ignored if ignore else None
            
            if dest.exists:
                dest.rm()
            
            logger.debug('..  cp: %s\n..      dest: %s', self.path, dest.path)
            
            shutil.copytree(self.path, dest.path, ignore = ignore)
    
    def empty(self):
        if self.exists:
            for root, dirs, files in walk(self.path):
                for d in dirs[:]:
                    if not d.startswith(('.', '_')):
                        Directory(abspath(root, d)).rm()
                    
                    dirs.remove(d)
                
                for f in files:
                    if not f.startswith(('.', '_')):
                        File(abspath(root, f)).rm()
    
    def mk(self):
        if not self.exists:
            logger.debug('..  mk: %s', self.path)
            
            makedirs(self.path)
    
    def rm(self):
        if self.exists:
            logger.debug('..  rm: %s', self.path)
            
            shutil.rmtree(self.path)
    
    
    @property
    def exists(self):
        return op.isdir(self.path)
    
    @property
    def is_root(self):
        return op.dirname(self.path) == self.path
    
    
    def __eq__(self, other):
        return self.path == other
    
    def __iter__(self):
        for root, dirs, files in walk(self.path):
            for d in dirs[:]:
                if d.startswith(('.', '_')):
                    dirs.remove(d)
            
            for f in files:
                if f.startswith(('.', '_')):
                    continue
                
                yield File(normpath(root, f))
    
    def __ne__(self, other):
        return self.path != other
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.path

class EventHandler(FileSystemEventHandler):
    def __init__(self, src, callback):
        self._src = src
        self._callback = callback
    
    
    def _regenerate(self, path):
        path = path.replace(self._src, '')
        
        if search(r'/[._](?!assets|containers|posts|templates)', path):
            logger.debug('>> Skipping: %s', path)
        else:
            logger.info('>> Change detected in: %s', path)
            
            try:
                Timer.start()
                
                self._callback()
                
                logger.info('Regenerated in %.3fs', Timer.stop())
            except:
                t, v, tb = exc_info()
                lc = traceback.extract_tb(tb)[-1:][0]
                
                logger.error('!! %s\n..  file: %s\n..  line: %s\n..    in: %s\n..    at: %s', v, *lc)
                
                pass
    
    
    def on_any_event(self, event):
        if event.event_type != 'moved':
            self._regenerate(event.src_path)
    
    def on_moved(self, event):
        self._regenerate(event.dest_path)

class File(object):
    def __init__(self, path, content = None):
        self.path = abspath(path)
        self.root = Directory(op.dirname(self.path))
        self.name, self.extension = op.splitext(op.basename(self.path))
        self.content = content
    
    
    def cp(self, dest):
        if self.exists:
            dest = File(dest)
            
            if self.path != dest.path:
                if not dest.root.exists:
                    dest.root.mk()
                
                logger.debug('..  cp: %s%s\n..      src:  %s\n..      dest: %s', self.name, self.extension, self.root, dest.root)
                
                shutil.copyfile(self.path, dest.path)
    
    def mk(self):
        if not self.exists:
            if not self.root.exists:
                self.root.mk()
            
            logger.debug('..  mk: %s', self.path)
            
            with open(self.path, 'w', encoding = 'utf-8') as f:
                if self.content is None:
                    self.content = ''
                
                f.write(self.content)
    
    def rm(self):
        if self.exists:
            logger.debug('..  rm: %s', self.path)
            
            remove(self.path)
    
    
    @property
    def content(self):
        if self._content is None and self.exists:
            with open(self.path, 'r', encoding = 'utf-8') as f:
                self._content = f.read()
        
        return self._content
    
    @content.setter
    def content(self, content):
        self._content = content
    
    @property
    def exists(self):
        return op.isfile(self.path)
    
    @property
    def mtime(self):
        if self.exists:
            return datetime.utcfromtimestamp(op.getmtime(self.path))
    
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.path
