def lengthOfPalindrome(input_string: str, left: int, right: int) -> int:
    """
    Will search the string and then return the length of the longest
    palindrome. Will start from the middle and keep expanding out till
    the characters are no longer a match.
    :param input_string: This is the input string
    :param left: This is the left pointer
    :param right: This is the right pointer
    :return: Length of the palindrome string
    """
    if (input_string is None) or (input_string == ""):
        return 0
    while (left >= 0 and right < len(input_string)) \
            and (input_string[left] == input_string[right]):
        left -= 1
        right += 1

    return right - left - 1


def longestPalindrome(s: str) -> str:
    s_length = len(s)

    if s is None or s_length < 1:
        return ""
    start = 0
    end = 0
    for i in range(s_length):
        len1 = lengthOfPalindrome(s, i, i)
        len2 = lengthOfPalindrome(s, i, i + 1)
        len_palindrome = len1 if len1 > len2 else len2
        if len_palindrome > (end - start):
            start = i - ((len_palindrome - 1) // 2)
            end = i + len_palindrome // 2
    return s[start:(end + 1)]


testPalindromeStrings = [
    "babad",
    "cbbd",
    "bbracecarcdc",
    "ac",
    "a",
    "bb"
]

for test in testPalindromeStrings:
    # test = "bb"
    print(longestPalindrome(test))
