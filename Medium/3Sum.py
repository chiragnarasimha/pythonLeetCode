import time
from typing import List

from ChiragHelperFunctions import printExecutionTime


def threeSumBruteForce(nums: List[int]) -> List[List[int]]:
    nums.sort()
    returnList: List = []
    for i, num1 in enumerate(nums):
        remainingElements = nums[i + 1:]
        for j, num2 in enumerate(remainingElements[1:]):
            if num1 + num2 + remainingElements[0] == 0:
                newList = [
                    num1,
                    remainingElements[0],
                    num2
                ]
                returnList.append(
                    newList) if newList not in returnList else None

    return returnList


startTime = time.time_ns()
threeSumBruteForce([-1, 0, 1, 2, -1, -4])
printExecutionTime(startTime)


# This is the optimal solution
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    returnList: List = []
    for i, num1 in enumerate(nums):
        remainingElements = nums[i + 1:]
        for j, num2 in enumerate(remainingElements[1:]):
            if num1 + num2 + remainingElements[0] == 0:
                newList = [
                    num1,
                    remainingElements[0],
                    num2
                ]
                returnList.append(
                    newList) if newList not in returnList else None

    return returnList
