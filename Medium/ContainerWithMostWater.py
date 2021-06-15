import time

from ChiragHelperFunctions import printExecutionTime


def maxAreaBruteForce(height) -> int:
    max_area = 0
    # lPoint = 0
    # rPoint = 0
    height_length = len(height)

    for i in range(height_length):
        for j in range(height_length):
            area = (j - i) * min(height[j], height[i])
            max_area = max(area, max_area)
    return max_area


startTime = time.time_ns()
result = maxAreaBruteForce([1, 8, 6, 2, 5, 4, 8, 3, 7])
printExecutionTime(startTime)


def maxArea(height: [int]) -> int:
    max_area = 0
    lPointer = 0
    rPointer = len(height) - 1
    while lPointer < rPointer:
        if height[lPointer] <= height[rPointer]:
            max_area = max(
                max_area,
                # This is the formula to calculate the area
                (rPointer - lPointer) * height[lPointer]
            )
            lPointer += 1
        else:
            max_area = max(
                max_area,
                # This is the formula to calculate the area
                (rPointer - lPointer) * height[rPointer]
            )
            rPointer -= 1
    return max_area


startTime = time.time_ns()
result = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
printExecutionTime(startTime)
