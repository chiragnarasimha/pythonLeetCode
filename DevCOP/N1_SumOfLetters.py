class N1_SumOfLetters:
    @staticmethod
    def letterSum(string):
        return sum([ord(char) - 96 for char in string])
