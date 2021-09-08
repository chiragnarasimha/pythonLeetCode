from typing import List


class N26:
    @staticmethod
    def removeDuplicates_IfWeHadLostsOfMemoryAvailable(nums: List[int]) -> int:

        return_list = []
        # duplicates_list = []

        for n in nums:
            if n not in return_list:
                return_list.append(n)
            # else:
            #     duplicates_list.append("_")
        return return_list

    def removeDuplicates(nums: List[int]) -> int:
        l_ptr = 1
        r_ptr = 0
        for r_ptr in range(1, len(nums)):
            if nums[r_ptr] != nums[r_ptr - 1]:
                nums[l_ptr] = nums[r_ptr]
                l_ptr += 1
                if r_ptr > len(nums):
                    break
        return nums[0:l_ptr]


print(N26.removeDuplicates([1, 1, 2]))
print(N26.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
