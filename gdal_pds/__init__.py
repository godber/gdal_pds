import numpy as np
from osgeo import gdal

from gdal_pds import label


class PDSImage(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.label = label.read(self.filepath)
        self._gdal_img = gdal.Open(filepath)
        self.num_bands = self._gdal_img.RasterCount
        self.image = self._band_data()

    def _band_data(self):
        """
        Returns the band data as a stacked Numpy Array
        """
        band_data_array = None
        # GDAL bands are numbered starting at 1
        for band in range(1, self.num_bands + 1):
            band_data = self._gdal_img.GetRasterBand(band).ReadAsArray()
            if band == 1:
                band_data_array = band_data
            else:
                band_data_array = np.dstack((self.image, band_data))
        return band_data_array
