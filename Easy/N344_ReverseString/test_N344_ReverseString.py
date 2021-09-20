import unittest

from Easy.N344_ReverseString.N344_ReverseString import N344


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = ["h", "e", "l", "l", "o"]
        N344.reverse_string(s)
        self.assertEqual(["o", "l", "l", "e", "h"], s)


if __name__ == '__main__':
    unittest.main()
