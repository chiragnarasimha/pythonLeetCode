from typing import List


class N136:
    @staticmethod
    def single_number_brute_force(nums: List[int]) -> int:

        history_map = {}
        for i, num, in enumerate(nums):
            if num in history_map:
                history_map.pop(num)
            else:
                history_map[num] = i

        return [k for k in history_map.keys()][0]

    @staticmethod
    def single_number(nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res
