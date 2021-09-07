import time

from ChiragHelperFunctions import print_execution_time


def intToRomanBruteForce(num: int) -> str:
    if num not in range(1, 4000):
        return " "
    romanCharacters = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M",
        2000: "MM",
        3000: "MMM",
    }
    resString = ""
    multiplier = 1
    while num != 0:
        rem = num % 10
        resString = romanCharacters[multiplier * rem] + resString
        multiplier *= 10
        num //= 10
    return resString


startTime = time.time_ns()
test = intToRomanBruteForce(1994)
test = intToRomanBruteForce(2000)
test = intToRomanBruteForce(3999)
test = intToRomanBruteForce(104)
print_execution_time(startTime)


def intToRoman(num: int) -> str:
    if num not in range(1, 4000):
        return " "
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", ]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", ]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", ]
    thousands = ["", "M", "MM", "MMM", ]
    return thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[
        (num % 100) // 10] + ones[(num % 10)]


startTime = time.time_ns()
test = intToRoman(1994)
test = intToRoman(2000)
test = intToRoman(3999)
test = intToRoman(104)
print_execution_time(startTime)


def intToRoman(num: int) -> str:
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
              (5, "V"), (4, "IV"), (1, "I")]
    roman_digits = []
    for val, symb in digits:
        if num >= val:
            count = num // val
            num -= count * val
            roman_digits.append(count * symb)
    return "".join(roman_digits)


startTime = time.time_ns()
test = intToRoman(1994)
test = intToRoman(2000)
test = intToRoman(3999)
test = intToRoman(133)
print_execution_time(startTime)
