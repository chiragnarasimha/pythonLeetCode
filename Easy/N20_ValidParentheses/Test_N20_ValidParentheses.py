import unittest

from Easy.N20_ValidParentheses.N20ValidParentheses import N20ValidParentheses


class TestSolution(unittest.TestCase):

    def test1(self):
        assert N20ValidParentheses.is_valid("(])").__eq__(False)
        assert N20ValidParentheses.is_valid("]").__eq__(False)
        assert N20ValidParentheses.is_valid("()").__eq__(True)
        assert N20ValidParentheses.is_valid("()[]{}").__eq__(True)
        assert N20ValidParentheses.is_valid("(]").__eq__(False)
        assert N20ValidParentheses.is_valid("([)]").__eq__(False)
        assert N20ValidParentheses.is_valid("{[]}").__eq__(True)
        assert N20ValidParentheses.is_valid("((").__eq__(False)

    def test2(self):
        assert True.__eq__(True)


if __name__ == '__main__':
    unittest.main()
