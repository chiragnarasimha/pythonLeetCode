class N344:
    @staticmethod
    def reverse_string(arr):
        l_ptr = 0
        r_ptr = len(arr) - 1
        while r_ptr > l_ptr:
            arr[l_ptr], arr[r_ptr] = arr[r_ptr], arr[l_ptr]
            l_ptr += 1
            r_ptr -= 1
