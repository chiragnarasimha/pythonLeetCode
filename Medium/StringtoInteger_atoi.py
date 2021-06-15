'''
https://leetcode.com/problems/string-to-integer-atoi/
'''
import re


def myAtoi(s: str) -> int:
    temp = re.search("(?<![\w .])(?<![+-])\s*[-+]?\d+", s)
    s = int(temp.group(0)) if temp else 0
    s = s if s > -2 ** 31 else -2 ** 31
    s = s if s < 2 ** 31 else 2 ** 31 - 1
    return s


# print(myAtoi("    10"))
# print(myAtoi("    -10"))
print(myAtoi("    -10 with words"))
print(myAtoi("    -10 with words"))
print(myAtoi(".1"))
# print(myAtoi("    "))
print(myAtoi("words and 987"))
print(myAtoi("+-987"))
print(myAtoi("0032"))
