import unittest
from datetime import date

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tire.octoprime import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):

        tire_ware_4_wheels = [0.9,0.8,0.7,0.6]
        tire = OctoprimeTire(tire_ware_4_wheels)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_ware_4_wheels = [0.9,0.8,0.7,0.5]
        tire = OctoprimeTire(tire_ware_4_wheels)
        self.assertFalse(tire.needs_service())
