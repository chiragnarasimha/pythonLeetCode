def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    # Add a new row till we hit the total number of rows
    str_array = [""] * numRows

    # At the start we are always going downwards
    goingDown = True
    row = 0
    for c in s:
        str_array[row] += c
        if goingDown or row == 0:
            row += 1
            goingDown = True

        else:
            row -= 1
            goingDown = False

        if row == numRows:
            row -= 2
            goingDown = False

    return "".join(str_array)


outp = [""] * 4
print(outp)
print(convert("PAYPALISHIRING", 4))
