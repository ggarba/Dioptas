__author__ = 'Clemens Prescher'

from Data.SpectrumData import Spectrum, SpectrumData, BkgNotInRangeError
import unittest
import numpy as np


class SpectrumDataTest(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(0.1, 15, 100)
        self.y = np.sin(self.x)
        self.spectrum = Spectrum(self.x, self.y)
        self.spectrum_data = SpectrumData()

    def test_spectrum_class(self):
        self.spectrum.save('Data/spec_test.txt')
        self.spectrum.save('Data/spec_test2.txt',
                           header='This is not only ridiculous\n but more and more '
                                  'challenging...')
        self.spectrum.load('Data/spec_test.txt', 0)
        self.spectrum.load('Data/spec_test2.txt', 0)

        self.assertTrue(np.array_equal(self.spectrum.data[0], np.linspace(0.1, 15, 100)))
        self.assertTrue(self.spectrum.load('Data/test_001.tif') == -1)

        self.spectrum.data = (np.linspace(0, 30), np.linspace(0, 20))
        self.spectrum.offset = 100
        self.assertTrue(np.array_equal(self.spectrum.data[1], np.linspace(0, 20) + 100))
        self.assertTrue(np.array_equal(self.spectrum.data[0], np.linspace(0, 30)))

        self.spectrum.scaling = 10
        self.assertTrue(np.array_equal(self.spectrum.data[1], np.linspace(0, 20) * 10 + 100))

        self.spectrum.data = (np.linspace(0, 20), np.linspace(0, 30))
        self.assertTrue(np.array_equal(self.spectrum.data[1], np.linspace(0, 30)))

        self.spectrum.scaling = -100
        self.assertTrue(np.array_equal(self.spectrum.data[1], np.zeros(self.spectrum.data[0].shape)))

    def test_spectrum_data_class(self):
        self.spectrum_data.set_spectrum(np.linspace(0, 10), np.linspace(0, 10) ** 2, 'SQUARED')
        self.spectrum_data.add_overlay(np.linspace(0, 10), np.linspace(0, 10) ** 3, 'CUBED')
        self.spectrum_data.add_overlay(np.linspace(0, 10), np.linspace(0, 10) ** 4, 'QUADRUPOLED')

        self.assertTrue(len(self.spectrum_data.overlays) == 2)
        self.spectrum_data.del_overlay(0)
        self.assertTrue(self.spectrum_data.overlays[0].name == 'QUADRUPOLED')

        self.spectrum_data.add_overlay_file('Data/spec_test2.txt')
        self.assertTrue(self.spectrum_data.overlays[-1].name == 'spec_test2')

    def test_background(self):
        x_spectrum = np.linspace(0,100,1001)
        y_spectrum = np.sin(x_spectrum)
        x_background = np.linspace(0,91, 1002)
        y_background = np.cos(x_background)

        spec = Spectrum(x_spectrum, y_spectrum)
        spec.set_background(Spectrum(x_background, y_background))

        x, y = spec.data

        self.assertTrue(x[-1]<1000)
        self.assertEqual(len(x), 911)

        test_x = np.linspace(0,91, 911)
        test_y = np.sin(test_x) - np.cos(test_x)

        diff = abs(np.sum(test_y-y))
        self.assertLess(diff, 1e-3)

    def test_background_not_in_spectrum_range(self):
        x_spectrum = np.linspace(0,30,101)
        y_spectrum = np.sin(x_spectrum)
        x_background = np.linspace(50,60, 102)
        y_background = np.cos(x_background)

        spec = Spectrum(x_spectrum, y_spectrum)
        spec.set_background(Spectrum(x_background, y_background))

        self.assertRaises(BkgNotInRangeError)








