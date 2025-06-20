import unittest
from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([7]), [7])

    def test_duplicates(self):
        self.assertEqual(selection_sort([3, 3, 2, 1]), [1, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()
