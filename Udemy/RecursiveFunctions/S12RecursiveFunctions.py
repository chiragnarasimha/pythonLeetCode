class S12:

    def __init__(self):
        self.factorial_sum = 1

    # def find_factorial_recursive(self, num):
    #     if num == 1 or num == 0:
    #         return self.factorial_sum
    #     else:
    #         self.factorial_sum *= num
    #         self.find_factorial_recursive(num - 1)
    #     return self.factorial_sum

    def find_factorial_recursive(self, num):
        if num == 1 or num == 0:
            return 1
        res = num * self.find_factorial_recursive(num - 1)
        return res

    @staticmethod
    def find_factorial_for_loop(num):
        if num == 1 or num == 0:
            return 1
        res = num
        while num > 1:
            num -= 1
            res *= num

        return res

    def get_fibonacci_number_at(self, index):
        if index < 2:
            return index

        return self.get_fibonacci_number_at(index - 1) + self.get_fibonacci_number_at(index - 2)

    @staticmethod
    def get_fibonacci_number_at_for_loop(index):

        if index == 0:
            return 0
        if index in [1, 2]:
            return 1
        prev_number, current_number, res = 0, 1, 1
        for _ in range(index - 1):
            # 0   1   2   3   4   5   6   7    8    9
            # 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 44
            res = prev_number + current_number
            prev_number = current_number
            current_number = res

        return res
