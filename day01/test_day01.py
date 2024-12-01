import unittest
from day01 import process_input

class TestDay01(unittest.TestCase):
    def test_with_example_input(self):
        # Read the test input file
        with open('test.txt', 'r') as file:
            lines = file.readlines()
        
        result = process_input(lines)
        expected = 11, 31  # whatever your expected result is
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 