import unittest

from Easy.N136_SingleNumber.N136_SingleNumber import N136


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, N136.single_number_brute_force([2, 2, 1]))
        self.assertEqual(4, N136.single_number_brute_force([4, 1, 2, 1, 2]))
        self.assertEqual(1, N136.single_number_brute_force([1]))

    def test_something2(self):
        self.assertEqual(1, N136.single_number([2, 2, 1]))
        self.assertEqual(4, N136.single_number([4, 1, 2, 1, 2]))
        self.assertEqual(1, N136.single_number([1]))


if __name__ == '__main__':
    unittest.main()
