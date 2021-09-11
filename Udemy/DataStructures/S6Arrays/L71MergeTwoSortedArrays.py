"""
Given two sorted arrays, can you merge them into a single array?
"""


class S6L71:
    @staticmethod
    def msa_chirag(arr1: [int], arr2: [int]):
        # Check the inputs

        if arr1 is None or len(arr1) == 0 and type(arr1) != [int]:
            return arr2
        if arr2 is None or len(arr2) == 0 and type(arr2) != [int]:
            return arr1

        # Create an array that is the length of the combined arrays
        # Create an array in advance
        merged_array = [None] * (len(arr1) + len(arr2))
        merged_array_ptr, arr1_ptr, arr2_ptr = 0, 0, 0

        while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
            if arr1[arr1_ptr] < arr2[arr2_ptr]:
                merged_array[merged_array_ptr] = arr1[arr1_ptr]
                arr1_ptr += 1
            # elif arr2[arr2_ptr] < arr1[arr1_ptr]:
            else:
                merged_array[merged_array_ptr] = arr2[arr2_ptr]
                arr2_ptr += 1

            merged_array_ptr += 1

            '''
            
            ***** Explanation ****
            
            The logic  below is unnecessary
                elif arr1[arr1_ptr] == arr2[arr2_ptr]:
                    merged_array[merged_array_ptr] = merged_array[
                        merged_array_ptr + 1] = arr1[arr1_ptr]
                    merged_array_ptr += 1
                    arr1_ptr += 1
                    arr2_ptr += 1
                merged_array_ptr += 1
            
            This is because once we move to the next item in the array, 
            if the value is less, then it will still continue will add it to 
            the merged array.
            
            for example, take [1,1,2,3] and [1,4]
            
                i1: arr1[0] = 1 is not less than arr2[0] = 1. Append arr2[0]
                i2: arr1[0] = 1 is less than arr2[1] = 4. Append arr1[0]
                i3: arr1[1] = 1 is less than arr2[1] = 4. Append arr1[1]
                
            '''

        if arr1_ptr < len(arr1):
            merged_array[merged_array_ptr:] = arr1[arr1_ptr:]
        if arr2_ptr < len(arr2):
            merged_array[merged_array_ptr:] = arr2_ptr[arr2_ptr:]

        return merged_array

    @staticmethod
    def msa_geeks_for_geeks(test_list1, test_list2):
        size_1 = len(test_list1)
        size_2 = len(test_list2)

        res = []
        i, j = 0, 0

        while i < size_1 and j < size_2:
            if test_list1[i] < test_list2[j]:
                res.append(test_list1[i])
                i += 1

            else:
                res.append(test_list2[j])
                j += 1

        res = res + test_list1[i:] + test_list2[j:]
        return res
