"""
Tests the image size and data.
"""

import unittest
import numpy as np

from gdal_pds import PDSImage


class TestImage(unittest.TestCase):

    def setUp(self):
        self.image_path = "test_data/1F345867992EFFB0J3P1212L0M1.img"
        self.pdsimage = PDSImage(self.image_path)
        #print self.label

    def test_image_size(self):
        """
        Verifies that the resulting image is an array of the correct dimensions
        """
        assert self.pdsimage.image.shape == (1024, 1024)

    def test_image_data_slice(self):
        """
        Verifies that a very small slice of the image array contains the correc
        values
        """
        slice = np.array(
            [[490, 473, 488, 485, 477],
             [458, 491, 482, 484, 490],
             [455, 467, 487, 480, 510],
             [459, 456, 526, 478, 486],
             [454, 482, 511, 456, 480]], dtype='int16'
        )
        assert np.array_equal(self.pdsimage.image[250:255, 250:255], slice)
