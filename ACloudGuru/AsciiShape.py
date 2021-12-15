length: int = 10
character: str = "*"
str_to_print: str = character
for i in range(length):
    spaceToPrepend = (" " * (length - i))
    print(spaceToPrepend + str_to_print)
    str_to_print += character + character

str_to_print = (2 * length - 1) * character
for i in range(length):
    spaceToPrepend = (" " * (i + 2))
    str_to_print = str_to_print[:-2]  # pop the last two characters everytime
    print(spaceToPrepend + str_to_print)
