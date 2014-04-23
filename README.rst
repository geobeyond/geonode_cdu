Geonode_Cdu
========================

geonode customization with cdu app.


Installation
------------

Install geonode with::

    $ sudo add-apt-repository ppa:geonode/testing

    $ sudo apt-get update

    $ sudo apt-get install geonode

Install django-django-wkhtmltopdf::

    $ pip install django-wkhtmltopdf



Install and start geonode_cdu::

    $ git clone https://github.com/pcasciano/geonode_cdu.git
    $ cd geonode_cdu
    $ python manage.py runserver

Usage
-----

set 'gisdata' database values in geonode_cdu/local_settings.py::

       'gisdata': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'database_name',
        'USER': 'geonode',
        'PASSWORD': 'geonode',
        'HOST': 'localhost',
        'PORT': '5432',
    }
