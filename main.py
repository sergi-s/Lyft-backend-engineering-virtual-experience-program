from test.test_battery.test_nubbin import TestNubbinBattery 
from test.test_battery.test_spindler import TestSpindlerBattery

from test.test_engine.test_capulet import TestCapuletEngine
from test.test_engine.test_sternman import TestSternmanEngine
from test.test_engine.test_willoughby import TestWilloughbyEngine


test_nubbin_battery = TestNubbinBattery()

test_nubbin_battery.test_needs_service_true()
test_nubbin_battery.test_needs_service_false()


test_Spindler_battery = TestSpindlerBattery()

test_Spindler_battery.test_needs_service_true()
test_Spindler_battery.test_needs_service_false()

test_capulet_engine = TestCapuletEngine()
test_capulet_engine.test_needs_service_true()
test_capulet_engine.test_needs_service_false()


test_Sternman_engine = TestSternmanEngine()
test_Sternman_engine.test_needs_service_true()
test_Sternman_engine.test_needs_service_false()


test_Willoughby_engine = TestWilloughbyEngine()
test_Willoughby_engine.test_needs_service_true()
test_Willoughby_engine.test_needs_service_false()