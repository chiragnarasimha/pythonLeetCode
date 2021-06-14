class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(list: ListNode):
    list_number = list.val
    while list_number is not None:
        print(list_number)
        list_number = list.next


class Solution:
    # # Step 1 is to determining which of these two files are bigger
    # def addTwoNumbers(self, list1: list, list2: list):
    #     list1_Length = len(list1)
    #     list2_Length = len(list2)
    #     list_result = list()
    #     carry_over = 0
    #     if list2_Length > list1_Length:
    #         print("list 2 is bigger")
    #         return self.addTwoNumbers(list2, list1)
    #     else:
    #         for i in range(list1_Length):
    #             if i < list2_Length:
    #                 sum_of_numbers = list1[i] + list2[i] + carry_over
    #             else:
    #                 sum_of_numbers = list1[i] + carry_over
    #             list_result.append(sum_of_numbers % 10)
    #             carry_over = sum_of_numbers // 10
    #             if (i == list1_Length - 1) and (carry_over != 0):
    #                 list_result.append(carry_over)
    #     return list_result

    # def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
    #     sum_result = ListNode(0)
    #     list1_number = list1.val
    #     list2_number = list2.val
    #     if list1 is None:
    #         return list2
    #     elif list2 is None:
    #         return list1
    #     else:
    #         while (list1_number is not None) or (list2_number is not None):
    #             sum_result.next = list1_number + list2_number
    #             sum_result.val = sum_result.next
    #             list1_number = list1.next
    #             list2_number = list2.next
    #
    #         sum_result.next = None
    #
    #     return sum_result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_result = ListNode()
        current = sum_result # This is used to add new elements to the list
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            temp = v1 + v2
            current.next = ListNode(temp % 10)
            carry = temp // 10
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sum_result.next # This will return the start of the sum list



if __name__ == '__main__':
    solution = Solution
    l1 = ListNode(2)
    l1.next = 4
    l1.next = 3
    l1.next = None

    l2 = ListNode(5)
    l2.next = 6
    l2.next = 4
    l2.next = None

    result = Solution.addTwoNumbers(l1, l1, l2)
    printList(result)

    # test=2+int(None)
    # print(test)
