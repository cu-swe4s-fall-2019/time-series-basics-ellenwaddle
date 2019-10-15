import data_import
import unittest
import sys
import os


class TestDataImport(unittest.TestCase):

    def test_data_print_array_linear(self):
        a = linear_search_value('this is not a time string')
        assertEquals(a, 'invalid time')


if __name__ == '__main__':
    unittest.main()
