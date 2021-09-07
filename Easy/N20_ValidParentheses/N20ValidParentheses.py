class N20ValidParentheses:
    @staticmethod
    def is_valid(s: str) -> bool:
        # This Dictionary contains all the matching pairs. This is also
        # scalable in the future if we need to add any further rules
        brackets_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # Store all the opening brackets in the stack
        stack = []
        for i in range(len(s)):
            # If we see a closing bracket, then we need to check the stack if
            # it contains a corresponding opening bracket. Only enter if the
            # stack contains any values initially
            if (s[i] in brackets_dict) and (len(stack) != 0):
                if stack[-1] == brackets_dict[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])

        return True if len(stack) == 0 else False


assert N20ValidParentheses.is_valid("]").__eq__(False)
assert N20ValidParentheses.is_valid("(])").__eq__(False)
assert N20ValidParentheses.is_valid("()").__eq__(True)
assert N20ValidParentheses.is_valid("))").__eq__(False)
assert N20ValidParentheses.is_valid("(]").__eq__(False)
assert N20ValidParentheses.is_valid("()[]{}").__eq__(True)
