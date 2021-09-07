from collections import deque


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

    @staticmethod
    # This was copied and pasted from leetcode
    def is_valid2(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        p = dict()
        p['('] = ')'
        p['{'] = '}'
        p['['] = ']'
        q = deque()
        for c in s:
            if c in p:
                q.append(c)
            elif q:
                if p[q.pop()] != c:
                    return False
            else:
                return False
        if q:
            return False
        return True
