#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 PyLadies, Lorena Mesa

from fabric import Connection, task
import patchwork.transfers

def setup_context(ctx):
    ctx.host = '81.28.232.189'
    ctx.user = 'u52703'
    ctx.connect_kwargs = {'key_filename': ['~/.ssh/pyladies.com']}
    return ctx

@task
def deploy(ctx):
    ctx = setup_context(ctx)
    with Connection(host=ctx.host, user=ctx.user, connect_kwargs=ctx.connect_kwargs) as connection:
        # Prep WWW Deploy
        connection.local('cd www && mynt gen -f _site')
        # Rsync WWW
        patchwork.transfers.rsync(connection, '_site/', 'www/', exclude='.git', rsync_opts='-ua')
