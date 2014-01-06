.. image:: https://travis-ci.org/godber/gdal_pds.png?branch=master   :target: https://travis-ci.org/godber/gdal_pds


gdal_pds
~~~~~~~~

A PDS Image library based on the GDAL implementation.

TODO
====

While this TODO section is present, this module is unstable since its being
worked on.::

    [ ] Fix multiline labels.
    [ ] Write tests for image data.
    [ ] Add tests for multiple instrument data files.
    [x] Write Sample data retrieval script.


Installation
============

Ubuntu
------

This should run with just the standard Ubuntu 12.04.3 versions of
``python-numpy`` and ``python-gdal`` which can be installed as follows::

    sudo apt-get update
    sudo apt-get install python-numpy python-gdal


Virtualenv
----------

This module can also be installed into a virtual environment.  The python
bindings for GDAL are a dependency for this project.  To install these on
Ubuntu 12.04.3 I first install the ubuntugis PPA::

    sudo apt-get update
    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    sudo apt-get update
    sudo apt-get build-dep python-numpy python-gdal
    sudo apt-get install libgdal1h libgdal1-dev python-gdal

Then create my virtualenv for the project and install the GDAL bindings in
the environment.  Make note of the environment variables that must be set
before building the GDAL bindings.::

    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    pip install -r requirements.txt

Note: If you were to just try and install the requirements without using the
unstable ubuntugis PPA, it would not build because the latest gdal python
bindings in PyPi do not build against the Ubuntu 12.04.3 libgdal package.  You
could probably force the proper version of the GDAL package to install and have
it work, but I have not tried it.  If you do find the working version please
let me know and I will update these instructions.

Vagrant
-------

The Vagrant file doesn't completely setup the project, one must manually run
the following commands after sshing to the vagrant box (`vagrant ssh`) to run
tests::

    mkvirtualenv gdal_pds
    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    cd /vagrant/
    pip install -r requirements.txt
    nosetests


Example Usage
=============

How to use gdal_pds::

    >>> from gdal_pds import PDSImage
    >>> image = PdsImage('1F345867992EFFB0J3P1212L0M1.img')
    # Returns a numpy array with the image data
    >>> image.data
    # returns the PDS Label as a Python dictionary
    >>> image.label
    >>> image.label['INSTRUMENT_ID']
    "FRONT_HAZCAM_LEFT"
    # Display the image
    >>> image.imshow()
