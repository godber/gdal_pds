from nose.tools import *
import gdal_pds

def test_gdal_present():
    try:
        from osgeo import gdal
    except:
        raise ImportError("GDAL not installed")
