import unittest

from Youtube.UnitTesting import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(15, calc.add(10, 5))
        self.assertEqual(0, calc.add(-1, 1))
        self.assertEqual(-2, calc.add(-1, -1))

    def test_subtract(self):
        self.assertEqual(5, calc.subtract(10, 5))
        self.assertEqual(-2, calc.subtract(-1, 1))
        self.assertEqual(0, calc.subtract(-1, -1))

    def test_multiply(self):
        self.assertEqual(50, calc.multiply(10, 5))
        self.assertEqual(-1, calc.multiply(-1, 1))
        self.assertEqual(1, calc.multiply(-1, -1))

    def test_divide(self):
        self.assertEqual(2, calc.divide(10, 5))
        self.assertEqual(-1, calc.divide(-1, 1))
        self.assertEqual(1, calc.divide(-1, -1))
        self.assertEqual(2.5, calc.divide(5, 2))

        """
        Testing the exceptions is a special case
        If we do
            self.assertRaises(ValueError, calc.divide(1,0))
        then the calc.divide will raise an exception and the test will 
        fail thinking that there is a legitimate exception without realising 
        that we are actually trying to test the exceptions        
        """

        self.assertRaises(ValueError, calc.divide, 10, 0)

        """
        Another way to test the same is by doing the following instead
        """
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
