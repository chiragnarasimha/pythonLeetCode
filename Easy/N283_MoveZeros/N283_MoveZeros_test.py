import unittest

from Easy.N283_MoveZeros.N283_MoveZeros import N283


class MyTestCase(unittest.TestCase):
    def test_move_zeroes_lazy(self):
        nums = [0, 1, 0, 3, 12]
        nums = N283.move_zeroes_lazy(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)

    def test_move_zeros_smarter_approach(self):
        nums = [0, 1, 0, 3, 12]
        nums = N283.move_zeros_smarter_approach(
            nums)

        self.assertEqual([1, 3, 12, 0, 0], nums)

        nums = [1, 3, 0, 12, 13, 14]
        nums = N283.move_zeros_smarter_approach(
            nums)
        print(nums)
        self.assertEqual([1, 3, 12, 13, 14, 0], nums)


if __name__ == '__main__':
    unittest.main()
