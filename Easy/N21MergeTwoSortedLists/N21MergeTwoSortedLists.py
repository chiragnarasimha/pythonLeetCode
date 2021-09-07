from typing import Optional

from ChiragHelperFunctions import ListNode


class N21:
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
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
        prev_node = ListNode()
        while (l1 is not None) and (l2 is not None):
            if l1.val > l2.val:
                current_node.val = l1.val
            