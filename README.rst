========================================
PyLadies: Website for our LA Women's Python Group
========================================

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

