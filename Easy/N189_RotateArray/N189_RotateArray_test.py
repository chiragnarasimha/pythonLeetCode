import unittest

from Easy.N189_RotateArray.N189_RotateArray import N189


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([5, 6, 7, 1, 2, 3, 4],
                         N189.rotate([1, 2, 3, 4, 5, 6, 7],
                                     3))
        self.assertEqual([-1, -100, 3, 99],
                         N189.rotate([3, 99, -1, -100],
                                     2))

        self.assertEqual([3, 99, -1, -100],
                         N189.rotate([-1, -100, 3, 99],
                                     2))

    if __name__ == '__main__':
        unittest.main()
