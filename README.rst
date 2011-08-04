<<<<<<< HEAD
====================
PyLadies.com Website
====================

This repo has moved from https://github.com/audrey/pyladies to https://github.com/pyladies/pyladies.  Please update your git config files.

Also, we are in the process of incorporating @maraujop's changes - significant work has been done, see https://github.com/maraujop/pyladies before doing major work.
=======
========================================
PyLadies: Website for the LA Women's Python Group
========================================
>>>>>>> aacfa884258616b79d15f692f090acca89a7354c

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
