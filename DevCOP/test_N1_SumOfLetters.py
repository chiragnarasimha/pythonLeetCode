import unittest

from DevCOP.N1_SumOfLetters import N1_SumOfLetters


class MyTestCase(unittest.TestCase):
    def test_findSum(self):
        self.assertEqual(N1_SumOfLetters.letterSum("jive"), 46)
        self.assertEqual(N1_SumOfLetters.letterSum("cop"), 34)
        

if __name__ == '__main__':
    unittest.main()
