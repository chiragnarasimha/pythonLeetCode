import time

from ChiragHelperFunctions import printExecutionTime


def multiplyBruteForce(num1: str, num2: str) -> str:
    # Subtracting ord(0) from a string will return the ascii integer value

    def parseNumber(s: str) -> int:
        """
        This will take in a single character and try to convert it to an integer
        :param s: Single character of the string
        :return: Character converted to integer
        """
        return ord(s) - ord("0")

    returnVal = 0
    for num1Index, num1Char in enumerate(reversed(num1)):
        tempVal = 0
        for num2Index, num2Char in enumerate(reversed(num2)):
            tempVal += 10 ** num2Index * (parseNumber(
                num1Char) * parseNumber(num2Char))
        returnVal += 10 ** num1Index * tempVal
    return str(returnVal)


"""
    12
  x 12
  -----
    24
   12+
  ----
  144 
"""
startTime = time.time_ns()
multiplyBruteForce("16", "16")
multiplyBruteForce("123", "456")
printExecutionTime(startTime)


def multiply(num1: str, num2: str) -> str:
    def parseNumber(s: str) -> int:
        """
        This will take in a string and convert it to int
        :param s: Single character of the string
        :return: Character converted to integer
        """
        returnVal = 0
        for c in s:
            returnVal = returnVal * 10 + (ord(c) - ord("0"))
        return returnVal

    return str(parseNumber(num1) * parseNumber(num2))


startTime = time.time_ns()
multiply("16", "16")
multiply("123", "456")
printExecutionTime(startTime)
