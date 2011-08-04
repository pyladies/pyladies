========================================
PyLadies Website
========================================

PyLadies is an international group of women who use and love the Python programming language. The main (pyladies.com) website is powered by Mezzanine (http://mezzanine.jupo.org/). Front-end design and development is by Christine Cheung (http://www.github.com/xtine) using HTML5Boilerplate and jQuery.


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

