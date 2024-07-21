"""Testing File for Problem 1 Solution"""
import unittest
from unittest import mock


class TestParser(unittest.TestCase):
    """Test Parser unit test class"""

    def setUp(self):
        self.data_lines = [
            'Cherry    4  1   Fruit  '
            'Pear      3  20  Fruit  '
            'Apple     10 5   Fruit  '
            'Banana    1  15   Fruit  '
        ]

        self.parsed_lines = [
            {'ItemName': 'Cherry', 'Price': '4', 'Quantity': '1', 'Category': 'Fruit'},
            {'ItemName': 'Pear', 'Price': '3', 'Quantity': '20', 'Category': 'Fruit'},
            {'ItemName': 'Apple', 'Price': '10', 'Quantity': '5', 'Category': 'Fruit'},
            {'ItemName': 'Banana', 'Price': '1', 'Quantity': '15', 'Category': 'Fruit'},
        ]

        self.file = mock.patch('builtins.open',
                new=mock.mock_open(read_data='\n'.join(self.data_lines)),
                create=True
        )

    def test_correct_stucture(self):
        """Test Parsing Fixed Width File Function for structure"""
        from main import parse_fixed_width_file

        with self.file:
            for record in parse_fixed_width_file('/dev/null'):
                self.assertEqual(4, len(record.keys()))
                self.assertListEqual(
                    ['ItemName', 'Price','Quantity','Category'],
                    list(record.keys())
                )


    def test_correct_values(self):
        """Test Parsing Fixed Width File Function for values"""
        from main import parse_fixed_width_file

        with self.file:
            for i, record in enumerate(parse_fixed_width_file('/dev/null')):
                self.assertDictEqual(record, self.parsed_lines[i])


if __name__ == '__main__':
    unittest.main()
