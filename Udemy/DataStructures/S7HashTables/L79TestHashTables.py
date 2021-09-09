import time
import unittest

from ChiragHelperFunctions import print_execution_time
from Udemy.DataStructures.S7HashTables.L79HashTables import HashTablesChirag

stress = 1000000


class TestS7HashTables(unittest.TestCase):

    def test_hash_functions(self):
        hash_table = HashTablesChirag(50)
        assert hash_table.get_key_hash("grapes") == 23
        assert hash_table.get_key_hash("grapess") == 13
        assert hash_table.get_key_hash("grapes3131s") == 21
        assert hash_table.get_key_hash("1232") == 2

    def test_set_and_get_functions(self):
        hash_table = HashTablesChirag(5)

        hash_table.set("g", 100)
        assert hash_table.get("g") == 100

        hash_table.set("g", 77)
        assert hash_table.get("g") == 77

        hash_table.set("a", 99)
        assert hash_table.get("a") == 99

        hash_table.set("a", 100)
        assert hash_table.get("a") == 100

        hash_table.set("abcd", 500)
        assert hash_table.get("abcd") == 500

        hash_table.set("higk", 1000)
        assert hash_table.get("higk") == 1000

        print("")
        print(hash_table)

    def test_get_keys_method(self):
        start = time.process_time_ns()
        hash_table = HashTablesChirag(5)

        list_of_keys = ["g", "a", "awa", "afgh", "aaas", "adsd", "affdfd",
                        "abcd", "higk", "babedd", ]

        for i, key in enumerate(list_of_keys):
            hash_table.set(key, 100 * i)

        print("")
        print_execution_time(start, "Time to setup data ")

        #     hash_table.get_keys()
        start = time.process_time_ns()
        assert sorted(hash_table.get_keys()) == sorted(list_of_keys)
        print_execution_time(start, "Time to sort the list and then make "
                                    "assertion")

        start = time.process_time_ns()
        hash_table.get_keys()
        print_execution_time(start, "Time to actually fetch the keys")
        # print(hash_table.get_keys())

        for i in range(stress):
            hash_table.get_keys()


if __name__ == '__main__':
    unittest.main()
