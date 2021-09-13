import unittest

from Udemy.DataStructures.S6Arrays.L71MergeTwoSortedArrays import S6L71


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.arr1 = [0, 3, 4, 31]
        self.arr2 = [4, 6, 30]
        self.test_class = S6L71()

    def test_chirag(self):
        self.assertEqual(self.arr1,
                         self.test_class.msa_chirag(self.arr1, []))

        self.assertEqual(self.arr2,
                         self.test_class.msa_chirag([], self.arr2))

        self.assertEqual([1, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                         self.test_class.msa_chirag([1, 3, 3, 5, 6, 9,
                                                     11],
                                                    [3, 4, 7, 8, 10]))

        self.assertEqual([0, 3, 4, 4, 6, 30, 31],
                         self.test_class.msa_chirag(self.arr1, self.arr2))

    def test_GeeksForGeeks(self):
        self.assertEqual([0, 3, 4, 4, 6, 30, 31],
                         self.test_class.msa_geeks_for_geeks(self.arr1,
                                                             self.arr2))

        self.assertEqual([1, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                         self.test_class.msa_geeks_for_geeks([1, 3, 3, 5, 6, 9,
                                                              11],
                                                             [3, 4, 7, 8, 10]))


if __name__ == '__main__':
    unittest.main()
