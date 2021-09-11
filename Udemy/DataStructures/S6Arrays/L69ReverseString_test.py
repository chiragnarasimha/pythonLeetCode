import unittest

from Udemy.DataStructures.S6Arrays.L69ReverseSring import S6L69

stress = 1


class MyTestCase(unittest.TestCase):
    def test_rev_py_built_in(self):
        for _ in range(stress):
            test_class = S6L69()

            self.assertEqual('ierdnA si eman yM iH',
                             test_class.rev_py_built_in('Hi My name is Andrei'))

    def test_rev_py_built_in2(self):

        for _ in range(stress):
            test_class = S6L69()

            self.assertEqual('ierdnA si eman yM iH',
                             test_class.rev_py_built_in2(
                                 'Hi My name is Andrei'))

            self.assertEqual(None,
                             test_class.rev_py_built_in2(None))

            self.assertEqual(None,
                             test_class.rev_py_built_in2(""))

            self.assertEqual(None,
                             test_class.rev_py_built_in2(123))

            self.assertEqual("a",
                             test_class.rev_py_built_in2("a"))

            self.assertEqual("ab",
                             test_class.rev_py_built_in2("ba"))


if __name__ == '__main__':
    unittest.main()
