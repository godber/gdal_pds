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

The python bindings for GDAL are a dependency for this project.  To install
these on Ubuntu 12.04.3 I first install the ubuntugis PPA::

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
    sudo apt-get update
    sudo apt-get install libgdal1-dev python-gdal

Then create my virtualenv for the project and install the GDAL bindings in
the environment.  Make note of the environment variables that must be set
before building the GDAL bindings.::

    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    pip install gdal


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
