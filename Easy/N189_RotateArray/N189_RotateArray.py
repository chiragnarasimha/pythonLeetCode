from typing import List


class N189:
    @staticmethod
    def rotate(nums: List[int], k: int) -> List[int]:
        # First determine how many times to actually rotate the given array
        k = k % len(nums)
        # Determine how to shift the array To modify the nums in place:
        # nums[::] = nums[len(nums) - k:] + nums[:len(nums) - k]
        return nums[len(nums) - k:] + nums[:len(nums) - k]
