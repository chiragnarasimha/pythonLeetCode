import unittest

from Udemy.RecursiveFunctions.S12RecursiveFunctions import S12


class TestRecursiveFunctions(unittest.TestCase):
    def setUp(self) -> None:
        # self.stress = 1
        self.stress = 1000000

    def test_find_factorial_recursive(self):
        s12 = S12()
        # s12.find_factorial_recursive(7)
        for _ in range(self.stress):
            self.assertEqual(5040, s12.find_factorial_recursive(7))
            self.assertEqual(1, s12.find_factorial_recursive(0))
            self.assertEqual(1, s12.find_factorial_recursive(1))
            self.assertEqual(2, s12.find_factorial_recursive(2))
            self.assertEqual(2432902008176640000, s12.find_factorial_recursive(20))
            self.assertAlmostEqual((6.0415263e+52 / 10 ** 52), s12.find_factorial_recursive(43) / 10 ** 52)
            self.assertAlmostEqual(6.0828186e+62 / 10 ** 62, s12.find_factorial_recursive(49) / 10 ** 62)

    def test_find_factorial_for_loop(self):
        s12 = S12()
        # s12.find_factorial_for_loop(7)
        for _ in range(self.stress):
            self.assertEqual(5040, s12.find_factorial_for_loop(7))
            self.assertEqual(1, s12.find_factorial_for_loop(0))
            self.assertEqual(1, s12.find_factorial_for_loop(1))
            self.assertEqual(2, s12.find_factorial_for_loop(2))
            self.assertEqual(2432902008176640000, s12.find_factorial_for_loop(20))
            self.assertAlmostEqual((6.0415263e+52 / 10 ** 52), s12.find_factorial_for_loop(43) / 10 ** 52)
            self.assertAlmostEqual(6.0828186e+62 / 10 ** 62, s12.find_factorial_for_loop(49) / 10 ** 62)

    def test_get_fibonacci_number_at(self):
        s12 = S12()
        # s12.find_factorial_recursive(7)
        self.assertEqual(0, s12.get_fibonacci_number_at(0))
        self.assertEqual(1, s12.get_fibonacci_number_at(1))
        self.assertEqual(1, s12.get_fibonacci_number_at(2))
        self.assertEqual(21, s12.get_fibonacci_number_at(8))
        self.assertEqual(2, s12.get_fibonacci_number_at(3))
        self.assertEqual(102334155, s12.get_fibonacci_number_at(40))

    def test_get_fibonacci_number_at_for_loop(self):
        s12 = S12()
        self.assertEqual(0, s12.get_fibonacci_number_at_for_loop(0))
        self.assertEqual(1, s12.get_fibonacci_number_at_for_loop(1))
        self.assertEqual(1, s12.get_fibonacci_number_at_for_loop(2))
        self.assertEqual(21, s12.get_fibonacci_number_at_for_loop(8))
        self.assertEqual(2, s12.get_fibonacci_number_at_for_loop(3))
        self.assertEqual(102334155, s12.get_fibonacci_number_at_for_loop(40))


if __name__ == '__main__':
    unittest.main()
