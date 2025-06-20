import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(bubble_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([4, 4, 3, 1]), [1, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()
