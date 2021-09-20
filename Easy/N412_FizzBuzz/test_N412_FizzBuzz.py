import unittest

from Easy.N412_FizzBuzz.N412_FizzBuzz import N412


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(["1", "2", "Fizz"], N412.fizz_buzz(3))  # add assertion here
        self.assertEqual(["1", "2", "Fizz", "4", "Buzz"], N412.fizz_buzz(5))  # add assertion here
        self.assertEqual(
            ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],
            N412.fizz_buzz(15))  # add assertion here


if __name__ == '__main__':
    unittest.main()
