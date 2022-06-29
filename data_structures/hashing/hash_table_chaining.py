# ********************************************
# Created by Mohammed Abdul Qavi on 29/06/22
# ********************************************


class HashTable(object):
    """
    A HashTable class that stores strings
    in a hash table, where keys are calculated
    using the first two letters of the string.
    Collision handling is performed by making using of the chaining strategy
    """

    def __init__(self):
        self.table = [[] for i in range(10000)]

    def store(self, string, value):
        """
        Function to store the given string and value to hash table
        """
        hash_value = self.calculate_hash_value(string)

        found = False
        for idx, element in enumerate(self.table[hash_value]):
            if len(element) and element[0] == string:
                self.table[hash_value][idx] = (string, value)
                found = True
                break

        if not found:
            self.table[hash_value].append((string, value))

    def lookup(self, string):
        """
        Return the hash value if the
        string is already in the table.
        Return -1 otherwise.
        """
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            for itr, element in enumerate(self.table[hash_value]):
                if len(element) and element[0] == string:
                    return self.table[hash_value][itr][1]
        else:
            return -1

    def calculate_hash_value(self, string):
        """
        Helper function to calulate a
        hash value from a string.
        """
        hash_value = 100 * ord(string[0]) + ord(string[1])
        return hash_value

    def delete(self, string):
        """
        Delete and return the element if the
        string is in the table.
        Return -1 otherwise.
        """

        hash_value = self.calculate_hash_value(string)
        for itr, element in enumerate(self.table[hash_value]):
            if len(element) and element[0] == string:
                return self.table[hash_value].pop(itr)

        return -1


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.store('UDACITY', 100)
    print(hash_table.lookup('UDACITY'))

    hash_val = hash_table.calculate_hash_value('UDACITY')

    hash_table.store('UDACIOUS', 200)
    print(hash_table.table[hash_val])

    print(hash_table.lookup('UDACIOUS'))
    print(hash_table.delete('UDACITY'))
    print(hash_table.table[hash_val])

"""
Output

100
[('UDACITY', 100), ('UDACIOUS', 200)]
200
('UDACITY', 100)
[('UDACIOUS', 200)]
"""
