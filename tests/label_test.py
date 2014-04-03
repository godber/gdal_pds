import unittest
from gdal_pds import label


class TestLabel(unittest.TestCase):

    def setUp(self):
        self.image_path = "test_data/1F345867992EFFB0J3P1212L0M1.img"
        self.label = label.read(self.image_path)
        #print self.label

    def test_instrument_id(self):
        assert self.label['COMMAND_SEQUENCE_NUMBER'] == '1'
        assert self.label['INSTRUMENT_ID'] == "FRONT_HAZCAM_LEFT"

    def test_wrapped_label(self):
        assert self.label['TELEMETRY_SOURCE_NAME'] == \
            '025_001_p1212-009-0001_003_0345867992-031.dat'

    def test_multiline_string_1(self):
        """
        This one is tricky because the continued string begins with a space
        on the second line, just using strip would consume this.
        """
        assert self.label['DATA_SET_NAME'] == \
            "MER 1 MARS HAZARD AVOIDANCE CAMERA EDR OPS VERSION 1.0"

    def test_multiline_string_2(self):
        assert self.label['PRODUCER_INSTITUTION_NAME'] == \
            'MULTIMISSION IMAGE PROCESSING SUBSYSTEM, JET PROPULSION LAB'
