
import unittest
from pharmacy import Drug, Pharmacy

class TestPharmacy(unittest.TestCase):
    def test_decrease_in_benefit_and_expires_in(self):
        initial_drug = Drug("test", 2, 3)
        pharmacy = Pharmacy([initial_drug])
        pharmacy.update_benefit_value()
        self.assertEqual(initial_drug.expires_in, 1)
        self.assertEqual(initial_drug.benefit, 2)

if __name__ == '__main__':
    unittest.main()
