# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         help(List)
from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:
#     answer_list = []
#     numbs_length = len(nums)
#     for i, item in enumerate(reversed(nums)):
#         difference = target - item
#         actual_i_in_numbs = numbs_length - 1 - i
#
#         remaining_numbs_array = nums[:actual_i_in_numbs]
#         if difference in remaining_numbs_array:
#             answer_list = [actual_i_in_numbs, i+remaining_numbs_array.index(difference)]
#             break
#         else:
#             answer_list = []
#
#     return answer_list

def twoSum(nums: List[int], target: int) -> List[int]:
    answer_list = []
    for index_num, num in enumerate(nums):
        reduced_nums_list = nums[index_num + 1:]
        diff = target - num
        if diff in reduced_nums_list:
            diff_index = reduced_nums_list.index(diff) + 1 + index_num
            answer_list = [index_num, diff_index]

    return answer_list

# Leet Code Solution
# def twoSum(nums: List[int], target: int) -> List[int]:
#     ref_map = {}
#
#     for idx, num in enumerate(nums):
#         target_sum = target - num
#         # print(target_sum)
#         if num in ref_map:
#             return [ref_map[num], idx]
#         else:
#             ref_map[target_sum] = idx
#         # print(ref_map)


l1 = [2, 7, 11, 15]
print(twoSum(l1, 9))

print(twoSum([3, 2, 4], 6))

print(twoSum([3, 3], 6))
