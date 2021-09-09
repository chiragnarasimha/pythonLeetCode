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
            # The modulo operator will ensure that the returned number will
            # stay within the length of the input data size
            hash_val = (hash_val + ord(key[i]) * i) % len(self.data)
        return hash_val

    def get_key_hash(self, key):
        return self.__generate_hash(key)

    def set(self, key, value):
        memory_address = self.__generate_hash(key)
        if self.data[memory_address] is None:
            self.data[memory_address] = [key, value]
        else:
            if key not in self.data[memory_address]:
                self.data[memory_address].append(key)
                self.data[memory_address].append(value)
                # self.data[memory_address].append([key, value])
            else:
                self.data[memory_address][
                    self.data[memory_address].index(key) + 1] = value

    def get(self, key):
        hash_val = self.__generate_hash(key)

        if self.data[hash_val] is None:
            return None
        else:
            return self.data[hash_val][self.data[hash_val].index(key) + 1]

    def get_keys(self):
        list_to_return = []
        for i in range(len(self.data)):
            if self.data[i] is not None:
                for k in self.data[i][::2]:
                    list_to_return.append(k)

        return list_to_return

    def get_keys2(self):
        """
        This is actually slower than just splicing the array. Refer to the
        test setup

        Also, need to check if this code even works :(
        :return:
        """
        list_to_return = []
        for i in range(len(self.data)):
            if self.data[i] is not None:
                for j in range(len(self.data[i])):
                    list_to_return.append(self.data[i][j])
                    j += 1

        return list_to_return
