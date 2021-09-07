import unittest

from Easy.N20_ValidParentheses.N20ValidParentheses import N20ValidParentheses

stress = 1000000


class TestSolution(unittest.TestCase):
    def test1(self):
        for _ in range(stress):
            assert N20ValidParentheses.is_valid("(])").__eq__(False)
            assert N20ValidParentheses.is_valid("]").__eq__(False)
            assert N20ValidParentheses.is_valid("()").__eq__(True)
            assert N20ValidParentheses.is_valid("()[]{}").__eq__(True)
            assert N20ValidParentheses.is_valid("(]").__eq__(False)
            assert N20ValidParentheses.is_valid("([)]").__eq__(False)
            assert N20ValidParentheses.is_valid("{[]}").__eq__(True)
            assert N20ValidParentheses.is_valid("((").__eq__(False)

    def test2(self):
        for _ in range(stress):
            assert N20ValidParentheses.is_valid2("(])").__eq__(False)
            assert N20ValidParentheses.is_valid2("]").__eq__(False)
            assert N20ValidParentheses.is_valid2("()").__eq__(True)
            assert N20ValidParentheses.is_valid2("()[]{}").__eq__(True)
            assert N20ValidParentheses.is_valid2("(]").__eq__(False)
            assert N20ValidParentheses.is_valid2("([)]").__eq__(False)
            assert N20ValidParentheses.is_valid2("{[]}").__eq__(True)
            assert N20ValidParentheses.is_valid2("((").__eq__(False)


if __name__ == '__main__':
    unittest.main()
