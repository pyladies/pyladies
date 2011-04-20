# deploy.wsgi is configured to live in pyladies/deploy.

import os

from os.path import abspath, dirname, join
from site import addsitedir

# Virtualenv pyladies is in ~/.virtualenvs
PROJECT_DIR = abspath(dirname(dirname(__file__)))
HOME_DIR = abspath(dirname(dirname(dirname(__file__))))
SITE_PACKAGES_DIR = abspath(join(dirname(dirname(dirname(__file__))), '.virtualenvs/pyladies/lib/python2.6/site-packages'))

addsitedir(SITE_PACKAGES_DIR)
addsitedir(HOME_DIR)
addsitedir(PROJECT_DIR)

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "pyladies.settings"

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
