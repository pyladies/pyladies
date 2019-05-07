#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 PyLadies, Lynn Root


from fabric.api import env, lcd, local
from fabric.contrib.project import rsync_project


env.user = "u52703"
env.keyfile_name = "~/.ssh/pyladies.com"
env.hosts = "81.28.232.189"


def prep_www_deploy():
    with lcd("www"):  # locally change into www dir
        local("mynt gen -f _site")


def rsync_www():
    with lcd("www"):
        rsync_project(local_dir="_site/",
                      remote_dir="www/",
                      extra_opts="-ua")


def deploy_www():
    prep_www_deploy()
    rsync_www()
