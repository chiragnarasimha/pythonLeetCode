def romanToInt(s: str) -> int:
    parseRomanNumber = {
        "": 0,
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    res = 0
    prevVal = 0
    for currChar in s:
        currVal = parseRomanNumber[currChar]
        res += currVal
        # Since we have incorrectly added the value, we need to correct the
        # mistake
        if prevVal < currVal:
            res -= 2 * prevVal
        prevVal = currVal
    return res


romanToInt("III")
romanToInt("IV")
romanToInt("IX")
romanToInt("LVIII")
romanToInt("MCMXCIV")
