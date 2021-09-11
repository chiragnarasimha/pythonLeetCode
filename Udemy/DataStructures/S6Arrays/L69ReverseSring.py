"""
Create a fuction that reverses a string:
'Hi My name is Andrei' should be:
'ierdnA si eman ¡H'
"""


class S6L69:
    @staticmethod
    def rev_py_built_in(string):
        ans = ""
        for s in string[::-1]:
            ans += s
        return ans

    @staticmethod
    def rev_py_built_in2(string):
        if string is None or string == "" or type(string) is not str:
            return None

        return string[::-1]
