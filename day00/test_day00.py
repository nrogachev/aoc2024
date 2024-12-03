from pathlib import Path
import unittest
from day00 import process_input

class TestDay00(unittest.TestCase):
    def test_with_example_input(self):
        file_path = Path(__file__).parent / 'test.txt'
        
        with open(file_path) as file:
            lines = file.readlines()
        
        result = process_input(lines)
        expected = 0, 0  # whatever your expected result is
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 