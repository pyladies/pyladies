#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 PyLadies, Lynn Root


from fabric.api import env, lcd, local
from fabric.contrib.project import rsync_project


env.user = "u52703"
env.keyfile_name = "~/.ssh/pyladies.com"
<<<<<<< HEAD
=======
env.hosts = "pyladies.com"
>>>>>>> ci-setup


def prep_www_deploy():
    with lcd("www"):  # locally change into www dir
        local("mynt gen -f _site")


def rsync_www():
    with lcd("www"):
        rsync_project(local_dir="_site",
<<<<<<< HEAD
                      remote_dir="u52703@pyladies.com:www/",
=======
                      remote_dir="www/",
>>>>>>> ci-setup
                      extra_opts="rupaz")


def deploy_www():
    prep_www_deploy()
    rsync_www()
