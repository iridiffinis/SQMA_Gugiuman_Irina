import unittest

class TestStringOperations(unittest.TestCase):
    def test_uppercase(self):
        """Test string uppercase conversion"""
        text = "hello"
        self.assertEqual(text.upper(), "HELLO")
        print("✓ Uppercase test passed")

    def test_concatenation(self):
        """Test string concatenation"""
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")
        print("✓ Concatenation test passed")

    def test_length(self):
        """Test string length"""
        text = "Jenkins"
        self.assertEqual(len(text), 7)
        print("✓ Length test passed")

if __name__ == '__main__':
    unittest.main()