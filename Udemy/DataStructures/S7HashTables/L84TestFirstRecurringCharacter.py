import unittest

from Udemy.DataStructures.S7HashTables.L84FirstRecurringCharacter import \
    L84FirstRecurringCharacter

stress = 1000000 * 3


class L84TestFirstRecurringCharacter(unittest.TestCase):
    def test_using_stacks(self):
        test_class = L84FirstRecurringCharacter()

        for _ in range(stress):
            self.assertEqual(2,
                             test_class.using_stacks(
                                 [2, 5, 1, 2, 3, 5, 1, 2, 4]),
                             )

            self.assertEqual(1,
                             test_class.using_stacks(
                                 [2, 1, 1, 2, 3, 5, 1, 2, 4]),
                             )

            self.assertEqual(None,
                             test_class.using_stacks([2, 3, 4, 5])
                             )

    def test_using_pointers(self):
        test_class = L84FirstRecurringCharacter()

        for _ in range(stress):
            self.assertEqual(2,
                             test_class.using_hash_tables(
                                 [2, 5, 1, 2, 3, 5, 1, 2, 4]),
                             )

            self.assertEqual(1,
                             test_class.using_hash_tables(
                                 [2, 1, 1, 2, 3, 5, 1, 2, 4]),
                             )

            self.assertEqual(None,
                             test_class.using_hash_tables([2, 3, 4, 5])
                             )


if __name__ == '__main__':
    unittest.main()
