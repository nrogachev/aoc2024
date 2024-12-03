import unittest
from day03 import process_input
import os

class TestDay03(unittest.TestCase):
    def test_with_example_input(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(current_dir, 'test2.txt')
        
        # Read the test input file
        with open(test_file_path, 'r') as file:
            lines = file.readlines()
        
        result = process_input(lines)
        expected = 161, 48  # whatever your expected result is
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 