class HashTablesChirag:
    def __init__(self, size):
        # This is used to predefine how much memory to allocate to this table
        # This is how we can preassigned the array
        self.data = [None] * size

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    # Private method to generate the hash key
    def __generate_hash(self, key):
        hash_val = 0
        for i in range(len(key)):
            hash_val = (hash_val + ord(key[i]) * i) % len(self.data)
        return hash_val

    def get_key_hash(self, key):
        return self.__generate_hash(key)

    def set(self, key, value):
        hash_val = self.__generate_hash(key)
        if self.data[hash_val] is None:
            self.data[hash_val] = [key, value]
        else:
            if key not in self.data[hash_val]:
                self.data[hash_val].append(key)
                self.data[hash_val].append(value)
            else:
                self.data[hash_val][self.data[hash_val].index(key) + 1] = value

    def get(self, key):
        hash_val = self.__generate_hash(key)

        if self.data[hash_val] is None:
            return None
        else:
            return self.data[hash_val][self.data[hash_val].index(key) + 1]
