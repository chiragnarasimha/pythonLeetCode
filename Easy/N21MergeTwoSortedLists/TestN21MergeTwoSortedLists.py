import unittest

from ChiragHelperFunctions import ListNode
from Easy.N21MergeTwoSortedLists.N21MergeTwoSortedLists import N21

stress = 1000000


class TestN21(unittest.TestCase):
    def test1(self):
        l1_3 = ListNode(4)
        l1_2 = ListNode(2, l1_3)
        l1_1 = ListNode(1, l1_2)

        l2_3 = ListNode(4)
        l2_2 = ListNode(3, l2_3)
        l2_1 = ListNode(1, l2_2)

        assert N21.merge_two_lists(l1_1, l2_1).__eq__([1, 1, 2, 3, 4, 4])

        l1_1 = None
        l2_1 = None
        assert N21.merge_two_lists(l1_1, l2_1).__eq__([])

        l1_1 = None
        l2_1 = ListNode(0)
        assert N21.merge_two_lists(l1_1, l2_1).__eq__([])
