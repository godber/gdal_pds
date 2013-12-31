import unittest
import gdal_pds


class TestGdalPds(unittest.TestCase):

    def setUp(self):
        self.image_path = "data/1F345867992EFFB0J3P1212L0M1.img"
        self.image = gdal_pds.PDSImage(self.image_path)

    def test_basic(self):
        assert self.image.filepath == self.image_path
