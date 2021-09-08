from typing import Optional

from ChiragHelperFunctions import ListNode


class N21:
    def merge_two_lists_chirag(self, l1: Optional[ListNode], l2: Optional[
        ListNode]) \
            -> Optional[ListNode]:
        # Initial checks to see if we even need to loop through the lists
        if l1 is None and l2 is None:
            return ListNode()

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        return_list = ListNode()

        # Current node will be used to loop through the return_list 
        current_node = return_list
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                current_node.val = l1.val
                l1 = l1.next
            elif l2.val < l1.val:
                current_node.val = l2.val
                l2 = l2.next
            elif l1.val == l2.val:
                current_node.val = l1.val
                current_node.next = ListNode(l1.val, None)
                current_node = current_node.next
                l1 = l1.next
                l2 = l2.next

            if l1 is not None and l2 is not None:
                current_node.next = ListNode()
                current_node = current_node.next

        while l1 is not None:
            current_node.val = l1.val
            if l1.next is not None:
                current_node.next = ListNode()
                current_node = current_node.next
            l1 = l1.next

        while l2 is not None:
            current_node.val = l1.val
            if l2.next is not None:
                current_node.next = ListNode()
                current_node = current_node.next
            l1 = l1.next

        return return_list

    @staticmethod
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[
        ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 is not None else l2

        return dummy.next
# n21 = N21()
# l1_3 = ListNode(4)
# l1_2 = ListNode(2, l1_3)
# l1_1 = ListNode(1, l1_2)
#
# l2_3 = ListNode(4)
# l2_2 = ListNode(3, l2_3)
# l2_1 = ListNode(1, l2_2)
#
# # assert n21.merge_two_lists(l1_1, l2_1).return_as_list().__eq__(
# #     [1, 1, 2, 3, 4, 4])
#
# print(n21.merge_two_lists(l1_1, l2_1).return_as_list())
