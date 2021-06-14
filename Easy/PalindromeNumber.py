def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    x = str(x)

    i = 0
    j = len(x) - 1

    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1

    return True


isPalindrome(1221)
isPalindrome(-1221)


def isPalindrome2(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)

    # def checkFromMiddle(s: str) -> bool:
    s_len = len(s)
    middle_index = s_len // 2
    left = 0
    right = 0
    if s_len % 2 == 0:
        left = middle_index - 1
        right = middle_index
    else:
        left = middle_index
        right = middle_index
    while left >= 0 and right < s_len:
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    return True


print(isPalindrome2(1221))
print(isPalindrome2(12221))
print(isPalindrome2(1122213))
print(isPalindrome2(10))
