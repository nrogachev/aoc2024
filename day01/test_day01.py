import unittest
from day01 import process_input
import os

class TestDay01(unittest.TestCase):
    def test_with_example_input(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(current_dir, 'test.txt')
        with open(test_file_path, 'r') as file:
            lines = file.readlines()
        result = process_input(lines)
        expected = 11, 31  
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 