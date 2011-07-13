====================
PyLadies.com Website
====================

This repo has moved from https://github.com/audrey/pyladies to https://github.com/pyladies/pyladies.  Please update your git config files.

Also, we are in the process of incorporating @maraujop's changes - significant work has been done, see https://github.com/maraujop/pyladies before doing major work.

The site is live at http://www.pyladies.com

How to download and run this locally
------------------------------------

Prerequisites: pip, virtualenv, virtualenvwrapper.

Installation::

    mkvirtualenv pyladies
    (then fork the repo and "git clone" your fork)
    cd pyladies
    pip install -r requirements.txt
    cp local_settings.py.example local_settings.py
    cp mezzanine.dbexample mezzanine.db
    python manage.py runserver
