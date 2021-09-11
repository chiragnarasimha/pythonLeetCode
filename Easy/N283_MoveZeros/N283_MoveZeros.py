from typing import List


class N283:
    @staticmethod
    def move_zeroes_lazy(nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        zeros = []
        for n in nums:
            if n != 0:
                res.append(n)
            else:
                zeros.append(0)
        return res + zeros

    @staticmethod
    def move_zeros_smarter_approach(nums: List[int]):
        anchor = 0
        print()
        for explorer, n in enumerate(nums):
            if n != 0:
                # Swap the two items

                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]

                anchor += 1
            # print(
            #     "{} | {} | nums = {}".format(
            #         explorer, anchor, nums))
            print(nums)
        return nums
