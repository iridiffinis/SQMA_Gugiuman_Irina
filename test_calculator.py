import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        """Test addition operation"""
        result = 2 + 2
        self.assertEqual(result, 4)
        print("Addition test passed")

    def test_subtraction(self):
        """Test subtraction operation"""
        result = 5 - 3
        self.assertEqual(result, 2)
        print("Subtraction test passed")

    def test_multiplication(self):
        """Test multiplication operation"""
        result = 3 * 4
        self.assertEqual(result, 12)
        print("Multiplication test passed")

if __name__ == '__main__':

    unittest.main()
