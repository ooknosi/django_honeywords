=================
Django Honeywords
=================

Django implementation of the `Honeywords Project`_ by Ari Juels and Ronald L. Rivest.

.. _Honeywords Project: http://people.csail.mit.edu/rivest/honeywords/

Generates a list of honeywords along with the actual user password on user registration. If the wrong compromised honeyword is used to login, the user account will be automatically deactivated.

Written for Django 2.2 on Python 3.6

Honeychecker Quick Link
-----------------------

`Honeychecker`__

__ honeychecker.py_

Quick Start
-----------
#) Install Django Honeywords::

    pip install django-honeywords

#) Add ``honeywords`` to ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = [
        ...
        'honeywords',
    ]

#) Create Honeywords table::

    ./manage.py makemigrations honeywords
    ./manage.py migrate

#) Add ``HONEYCHECKER_URI = http(s)://<url/ip>:<port>`` into ``settings.py``::

    HONEYCHECKER_URI = 'http://192.168.56.101:55555'

#) Add ``honeywords.backends.HoneywordsBackend`` to the top of ``AUTHENTICATION_BACKENDS`` in ``settings.py`` (or add ``AUTHENTICATION_BACKENDS`` if missing)::

    AUTHENTICATION_BACKENDS = [
       'honeywords.backends.HoneywordsBackend',
       'django.contrib.auth.backends.ModelBackend',
       ]

#) Download `honeychecker.py`_ to the Honeychecker server.

    .. _honeychecker.py: https://raw.githubusercontent.com/ooknosi/django_honeywords/master/src/honeywords/honeychecker.py

#) Edit the ``IP``, ``PORT`` and ``DATABASE`` settings in ``honeychecker.py``::

    ### Settings
    IP = '192.168.56.101'
    PORT = 55555
    DATABASE = 'honeychecker_db.sqlite3'
    ###

#) Run ``honeychecker.py`` on the Honeychecker server::

    python honeychecker.py

Documentation
-------------
TODO
