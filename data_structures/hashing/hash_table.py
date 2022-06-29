# ********************************************
# Created by Mohammed Abdul Qavi on 29/06/22
# ********************************************

class HashTable(object):
    """
    A HashTable class that stores strings
    in a hash table, where keys are calculated
    using the first two letters of the string.
    """

    def __init__(self):
        self.table = [None] * 10000

    def store(self, string, value):
        """
        Function to store the given string and value to hash table
        """
        hash_value = self.calculate_hash_value(string)
        self.table[hash_value] = value

    def lookup(self, string):
        """
        Return the hash value if the
        string is already in the table.
        Return -1 otherwise.
        """
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            return self.table[hash_value]
        else:
            return -1

    def calculate_hash_value(self, string):
        """
        Helper function to calculate a
        hash value from a string.
        """
        hash_value = 31 * ord(string[0]) + ord(string[1])
        return hash_value


if __name__ == "__main__":
    hash_table = HashTable()
    print(
        "The hash value for the given string is {}".format(
            hash_table.calculate_hash_value('UDACITY')
        )
    )
    print(hash_table.lookup('UDACITY'))

    hash_table.store('UDACITY', 100)
    print(hash_table.lookup('UDACITY'))

    hash_table.store('UDACIOUS', 101)
    print(hash_table.lookup('UDACIOUS'))

"""
Output

The hash value for the given string is 2703
-1
100
101
"""
