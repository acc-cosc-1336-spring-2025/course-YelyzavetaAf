import unittest
from src.homework.i_dictionaries_sets import dictionary

class TestInventoryFunctions(unittest.TestCase):

    def test_add_inventory(self):
        widgets = {}
        dictionary.add_inventory(widgets, "Widget1", 10)
        self.assertEqual(widgets["Widget1"], 10)

        dictionary.add_inventory(widgets, "Widget1", 25)
        self.assertEqual(widgets["Widget1"], 35)

        dictionary.add_inventory(widgets, "Widget1", -10)
        self.assertEqual(widgets["Widget1"], 25)

    def test_remove_inventory_widget(self):
        widgets = {"Widget1": 10, "Widget2": 20}
        result = dictionary.remove_inventory_widget(widgets, "Widget1")
        self.assertEqual(result, "Record deleted")
        self.assertNotIn("Widget1", widgets)
        self.assertIn("Widget2", widgets)

        result_not_found = dictionary.remove_inventory_widget(widgets, "Widget3")
        self.assertEqual(result_not_found, "Item not found")