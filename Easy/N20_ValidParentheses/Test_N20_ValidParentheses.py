import unittest

from Easy.N20_ValidParentheses.N20ValidParentheses import N20ValidParentheses


class TestSolution(unittest.TestCase):

    def test1(self):
        sol = N20ValidParentheses()
        assert sol.is_valid("(])").__eq__(False)
        assert sol.is_valid("]").__eq__(False)
        assert sol.is_valid("()").__eq__(True)
        assert sol.is_valid("()[]{}").__eq__(True)
        assert sol.is_valid("(]").__eq__(False)
        assert sol.is_valid("([)]").__eq__(False)
        assert sol.is_valid("{[]}").__eq__(True)
        assert sol.is_valid("((").__eq__(False)

    def test2(self):
        assert True.__eq__(True)


if __name__ == '__main__':
    unittest.main()
