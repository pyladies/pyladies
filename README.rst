========================================
PyLadies: Website for the LA Women's Python Group
========================================

This is my version of the PyLadies website with cleaned up CSS and JS using the HTML5 Boilerplate. My spin on a new clean design inspired by the original look as well as the fork by maraujop.


How to Use
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

