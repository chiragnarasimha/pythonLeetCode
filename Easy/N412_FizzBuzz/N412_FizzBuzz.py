from typing import List


class N412:
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:

        res = []
        for i in range(1, n + 1):
            mod3 = i % 3
            mod5 = i % 5
            if mod3 == 0 and mod5 != 0:
                res.append("Fizz")
            elif mod5 == 0 and mod3 != 0:
                res.append("Buzz")
            elif mod3 == 0 and mod5 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))
        return res
