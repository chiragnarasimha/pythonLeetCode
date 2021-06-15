'''
If it is a dot then there is no need to check if the string matches
'''


def isMatch(s: str, p: str) -> bool:
    s_pointer = 0
    p_pointer = 0
    while s_pointer < len(s) and p_pointer < len(p):
        pchar = p[p_pointer]
        if pchar == ".":
            s_pointer += 1
            p_pointer += 1
            break  # TODO: Unfinished code
    return True


isMatch("aa", ".a")
