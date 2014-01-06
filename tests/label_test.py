import unittest
from gdal_pds import label


class TestLabel(unittest.TestCase):

    def setUp(self):
        self.image_path = "test_data/1F345867992EFFB0J3P1212L0M1.img"
        self.label = label.read(self.image_path)

    def test_instrument_id(self):
        assert self.label['COMMAND_SEQUENCE_NUMBER'] == '1'
        assert self.label['INSTRUMENT_ID'] == "FRONT_HAZCAM_LEFT"
