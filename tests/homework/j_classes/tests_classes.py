import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_value_range(self):
        die = Die()
        for _ in range(3):
            die.roll()
            value = die.get_rolled_value()
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)