#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 PyLadies, Lorena Mesa

from fabric import Connection
import patchwork.transfers


def deploy_www():
    connect_kwargs = {'key_filename': ['~/.ssh/pyladies.com']}
    with Connection(host='81.28.232.189', user='u52703', connect_kwargs=connect_kwargs) as connection:
        # Prep WWW Deploy
        connection.cwd('www')
        connection.local('mynt gen -f _site')
        # Rsync WWW
        patchwork.transfers.rsync(connection, '_site/', 'www/', exclude='.git', rsync_opts='-ua')
