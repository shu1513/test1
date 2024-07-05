# test_math_operations.py
import unittest
import logging
from math_operations import divide

# Set up logging for unit tests
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMathOperations(unittest.TestCase):

    def test_divide_normal(self):
        logging.info("Testing divide with normal values")
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_zero(self):
        logging.info("Testing divide by zero")
        self.assertIsNone(divide(10, 0))

    def test_divide_negative(self):
        logging.info("Testing divide with negative values")
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)

if __name__ == '__main__':
    unittest.main()
