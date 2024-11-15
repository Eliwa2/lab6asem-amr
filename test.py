# test.py
import unittest
from calculator import Calc  # Import the Calc class correctly

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calc.add(2, 2)
        self.assertEqual(result, 4)

if _name_ == '_main_':
    unittest.main()  # Call unittest.main() properly
    