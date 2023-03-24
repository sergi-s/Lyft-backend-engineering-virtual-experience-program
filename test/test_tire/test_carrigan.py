import unittest
from datetime import date

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from tire.carrigan import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_ware_4_wheels = [0,1,0.1,0.3]
        tire = CarriganTire(tire_ware_4_wheels)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_ware_4_wheels = [0.1,0.3,0.2,0.3]
        tire = CarriganTire(tire_ware_4_wheels)
        self.assertFalse(tire.needs_service())
