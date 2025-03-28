import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

class TestListFunctions(unittest.TestCase):
    def test_lowest(self):
        self.assertEqual(get_lowest_list_value([8, 10, 1, 50, 20]), 1)


    def test_highest(self):
        self.assertEqual(get_highest_list_value([8, 10, 1, 50, 20]), 50)