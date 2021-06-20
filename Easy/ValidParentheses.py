import re
import time

from ChiragHelperFunctions import printExecutionTime


def isValidBruteForceå(s: str) -> bool:
    # Initial Validation to check s
    if s == '' or not s:
        return False
    # Make sure that we are only checking the parentheses
    matches = re.findall(r"[\(\)\{\}\[\]]+", s)
    s = ''.join(matches) if matches else None

    # Check to make sure that there are even number of parentheses
    if len(s) % 2 != 0:
        return False

    # At this point, we have already processed the string to only contain the
    # brackets
    closingStack = []
    for char in s:
        closingStack.append(char) if char in ["(", '{', '['] else None
        if char == ')':
            if closingStack and closingStack[-1] == '(':
                closingStack.pop()
            else:
                return False
        if char == '}':
            if closingStack and closingStack[-1] == '{':
                closingStack.pop()
            else:
                return False
        if char == ']':
            if closingStack and closingStack[-1] == '[':
                closingStack.pop()
            else:
                return False
    # At the end, the stack should not contain any values
    return True if not closingStack else False


startTime = time.time_ns()
print(isValidBruteForceå("(}})"))
print(isValidBruteForceå('()'))
print(isValidBruteForceå('()[]{}'))
print(isValidBruteForceå('(]'))
print(isValidBruteForceå('([)]'))
print(isValidBruteForceå('{[]}'))
print(isValidBruteForceå('()'))
print(isValidBruteForceå(']'))
print(isValidBruteForceå('[(test)(){}(t[1])]'))
printExecutionTime(startTime)

print('-' * 80)


def isValid(s: str) -> bool:
    # Initial Validation to check s
    if s == '' or not s:
        return False
    # Make sure that we are only checking the parentheses
    matches = re.findall(r"[\(\)\{\}\[\]]+", s)
    s = ''.join(matches) if matches else None

    # Check to make sure that there are even number of parentheses
    if len(s) % 2 != 0:
        return False
    
    stack = []
    closeToOpen = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for c in s:
        # Start by first checking if we have hit a closing bracket already
        if c in closeToOpen:
            # If we have hit a closing bracket, then
            #   1. The stack should not be empty
            #   2. The last item in the stack must be equal to the
            #      opening bracket
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


startTime = time.time_ns()
print(isValid("(}})"))
print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid('()'))
print(isValid(']'))
print(isValid('[(test)(){}(t[1])]'))
printExecutionTime(startTime)
