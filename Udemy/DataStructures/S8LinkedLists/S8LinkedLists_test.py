import unittest

from Udemy.DataStructures.S8LinkedLists.S8LinkedLists import LinkedList


class MyTestCase(unittest.TestCase):
    def test_basic_validations(self):
        self.assertEqual(True, True)
        list1 = LinkedList(10)
        self.assertEqual(10, list1.head.val)

    def test_for_just_one_node(self):
        list1 = LinkedList(10)
        self.assertEqual(10, list1.head.val)
        self.assertEqual(10, list1.tail.val)

    def test_append_feature(self):
        list1 = LinkedList("a")
        list1.append("b")
        self.assertEqual("a", list1.head.val)
        self.assertEqual("b", list1.tail.val)
        list1.append("c")
        self.assertEqual("a", list1.head.val)
        self.assertEqual("c", list1.tail.val)

    def test_get_node(self):
        list1 = LinkedList(0)
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        self.assertEqual(0, list1.get_node(0).val)
        self.assertEqual(3, list1.get_node(3).val)

    def test_insert_featue(self):
        list1 = LinkedList("a")
        list1.append("b")
        list1.append("d")
        list1.insert("c", 2)
        self.assertEqual("[ a b c d ]", list1.to_str())
        self.assertEqual("d", list1.tail.val)

        list2 = LinkedList("2")
        list2.append("3")
        list2.append("4")
        list2.append("5")
        list2.prepend("1")
        list2.prepend("0")
        self.assertEqual("[ 0 1 2 3 4 5 ]", list2.to_str())
        list2.insert("a", 2)
        self.assertEqual("[ 0 1 a 2 3 4 5 ]", list2.to_str())
        self.assertEqual(7, list2.length)

    def test_insert_exception_handling(self):
        list1 = LinkedList("a")
        list1.append("b")
        list1.append("d")
        list1.insert("c", 2)
        list1.append("f")
        list1.insert("e", 4)
        self.assertEqual("[ a b c d e f ]", list1.to_str())

        with self.assertRaises(SyntaxError):
            list1.insert(0, 0)

    def test_prepend(self):
        list1 = LinkedList("b")
        list1.append("c")
        list1.append("d")
        self.assertEqual("[ b c d ]", list1.to_str())
        list1.prepend("a")
        self.assertEqual("a", list1.head.val)
        self.assertEqual("[ a b c d ]", list1.to_str())


if __name__ == '__main__':
    unittest.main()
