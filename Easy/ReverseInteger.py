"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-2^31 <= x <= 2^31 - 1

"""


def reverse(x: int) -> int:
    answer = 0
    negative = -1 if x < 0 else 1
    x *= negative
    while x != 0:
        answer *= 10
        answer += x % 10
        x //= 10
    answer *= negative
    return answer if answer in range(-2 ** 31, 2 ** 31) else 0


print(2 ** 31 - 1)
print(-2 ** 31)

print(1563847412 > 2 ** 31)

for i in [123, -123, 120, 0, 1534236469]:
    print(reverse(i))
