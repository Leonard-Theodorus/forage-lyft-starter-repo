import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

class TestCarriganTires(unittest.TestCase):
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.2, 0.001, 0.44, 0.55123]
        service = False
        for wear in tire_wear:
            if wear >= 0.9:
                service = True
                break
        self.assertFalse(service)

    def test_tire_should_be_serviced(self):
        tire_wear = [0.2, 0.001, 1, 0.998]
        service = False
        for wear in tire_wear:
            if wear >= 0.9:
                service = True
                break
        self.assertTrue(service)

class TestOctoprimeTires(unittest.TestCase):
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.2, 0.001, 1, 0.55123]
        service = True if sum(tire_wear) >= 3 else False
        self.assertFalse(service)

    def test_tire_should_be_serviced(self):
        tire_wear = [0.9, 1, 0.855, 0.998]
        service = True if sum(tire_wear) >= 3 else False
        self.assertTrue(service)


if __name__ == "__main__":
    unittest.main()