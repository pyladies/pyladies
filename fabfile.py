#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 PyLadies, Lorena Mesa

from fabric import Connection, task
import patchwork.transfers

def setup_context(ctx):
    ctx.host = '81.28.232.189'
    ctx.user = 'u52703'
    return ctx

@task
def deploy(ctx):
    ctx = setup_context(ctx)
    with Connection(host=ctx.host, user=ctx.user) as connection:
        # Rsync WWW
        patchwork.transfers.rsync(connection, 'www/_site/', 'www/', exclude='.git', rsync_opts='-ua')
