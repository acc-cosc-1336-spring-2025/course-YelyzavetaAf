import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value, get_p_distance, get_p_distance_matrix

class TestListFunctions(unittest.TestCase):
    def test_lowest(self):
        self.assertEqual(get_lowest_list_value([8, 10, 1, 50, 20]), 1)


    def test_highest(self):
        self.assertEqual(get_highest_list_value([8, 10, 1, 50, 20]), 50)

    
    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        result = get_p_distance(list1, list2)
        expected = 0.4
        self.assertAlmostEqual(result, expected, places=3)


    def test_get_p_distance_matrix(self):
        sequences = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result_matrix = get_p_distance_matrix(sequences)

    
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix)):
                self.assertAlmostEqual(result_matrix[i][j], expected_matrix[i][j], places=3)

