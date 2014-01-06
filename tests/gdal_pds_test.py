import unittest
import gdal_pds


class TestGdalPds(unittest.TestCase):

    def setUp(self):
        self.image_path = "test_data/1F345867992EFFB0J3P1212L0M1.img"
        self.image = gdal_pds.PDSImage(self.image_path)

    def test_image_path(self):
        assert self.image.filepath == self.image_path

    def test_num_bands(self):
        assert self.image.num_bands == 1

    def test_instrument_id(self):
        assert self.image.label['INSTRUMENT_ID'] == "FRONT_HAZCAM_LEFT"
