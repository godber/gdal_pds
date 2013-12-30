gdal_pds
~~~~~~~~

A PDS Image library based on the GDAL implementation.

Installation
============

The python bindings for GDAL are a dependency for this project.  To install
these on Ubuntu 12.04.3 I first install the ubuntugis PPA
::

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:ubuntugis/ppa

Then create my virtualenv for the project and install the GDAL bindings in
the environment.  Make note of the environment variables that must be set
before building the GDAL bindings.
::

  export CPLUS_INCLUDE_PATH=/usr/include/gdal
  export C_INCLUDE_PATH=/usr/include/gdal
  pip install GDAL


Example Usage
=============
