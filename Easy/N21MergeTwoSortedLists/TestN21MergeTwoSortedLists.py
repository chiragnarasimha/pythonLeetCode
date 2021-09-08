import unittest

from ChiragHelperFunctions import ListNode, list_node_to_array
from Easy.N21MergeTwoSortedLists.N21MergeTwoSortedLists import N21

stress = 1000000


class TestN21(unittest.TestCase):
    def test1(self):
        n21 = N21()
        l1_3 = ListNode(4)
        l1_2 = ListNode(2, l1_3)
        l1_1 = ListNode(1, l1_2)

        l2_3 = ListNode(4)
        l2_2 = ListNode(3, l2_3)
        l2_1 = ListNode(1, l2_2)

        assert list_node_to_array(n21.merge_two_lists(l1_1,
                                                      l2_1)) \
               == [1, 1, 2,
                   3, 4, 4]

        l1_1 = None
        l2_1 = None
        assert list_node_to_array(n21.merge_two_lists(l1_1,
                                                      l2_1)) \
               == []

        l1_1 = None
        l2_1 = ListNode(0)
        assert list_node_to_array(n21.merge_two_lists(l1_1,
                                                      l2_1)) \
               == [0]
