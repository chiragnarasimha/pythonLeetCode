"""
This question was asked in google interview

Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2
Given an array = 12,1,1,2,3,5,1,2,4]:
It should return 1
Given an array = [2,3,4,5]:
It should return undefined

"""


class L84FirstRecurringCharacter:
    def __init__(self):
        """
        There is nothing to initialise
        """
        pass

    @staticmethod
    def using_stacks(nums: [int]):
        history_stack = []
        for n in nums:
            if n not in history_stack:
                history_stack.append(n)
            else:
                return n
        return None

    @staticmethod
    def using_hash_tables(nums: [int]):
        history_map = {}
        for i, n in enumerate(nums):
            if n not in history_map:
                history_map[n] = i
            else:
                return n
        return None

    @staticmethod
    def using_for_loops(nums: [int]):
        """
        To fix this, we need to calculate the distance between each as we
        loop through
        function firstRecurringCharacter2(array) {

            let lastPair = undefined;
            let lastDistance = undefined;
            for(let i = 0; i < array.length; i++) {
                for(let j = i+1; j < array.length; j++) {
                    if(array[i] === array[j] && (lastDistance>j-i || lastDistance==undefined)) {
                        lastPair=array[i];
                        lastDistance= j-i;
                        break;
                    }
                }
            }
            return lastPair;
        }
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        return None
