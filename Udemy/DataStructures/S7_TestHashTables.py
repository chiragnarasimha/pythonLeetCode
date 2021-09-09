import unittest

from Udemy.DataStructures.S7_HashTables import HashTablesChirag


class S7TestHashTables(unittest.TestCase):
    def test_hash_functions(self):
        hash_table = HashTablesChirag(50)
        assert hash_table.get_key_hash("grapes") == 23
        assert hash_table.get_key_hash("grapess") == 13
        assert hash_table.get_key_hash("grapes3131s") == 21
        assert hash_table.get_key_hash("1232") == 2

    def test_set_and_get_functions(self):
        hash_table = HashTablesChirag(50)

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


if __name__ == '__main__':
    unittest.main()
