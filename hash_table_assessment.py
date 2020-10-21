'''
Write a program that creates a stem-and-leaf diagram using the data provided below:
    a. https://en.wikipedia.org/wiki/Stem-and-leaf_display
        i. Every stem should be listed once, even if it has no leaves.
        ii. Duplicate valued leaves should be listed multiple times.
    b. Your program must implement a sorting algorithm to sort the data into ascending order.
    c. Your program must then apply a hashing algorithm or function to the data to construct the
       stem-and-leaf data structure representation. Print out the data distribution.
    d. Your program must use a searching algorithm to allow the user to search for a particular value in the data set.

Sample input data:
36 29 31 125 139 131 115 105 111 40 119 47 105 57 122 109 124 115 43 120 43 27 27 32 61 37 127 29 113 121 58 114 126 53 114 96 12 127 28 42 39 113 42 18 44 18 28 48 125 107 114 34 33 45 120 30 127 31 116 146 58 109 23 105 63 27 44 105 99 41 128 121 116 125 118 44 37 113 124 37 48 127 25 109 7 31 141 46 13 27 43 117 116 27 7 68 40 31 115 124 42 128 52 71 118 117 38 27 106 33 117 116 132 104 123 35 113 122 42 117 119 32 61 37 127 29 113 121 58 114 126 53 114 96

Notice that there are duplicate values in the input data (e.g., 127) so your program must be able to handle hash code collisions in the data structure.

'''


class Hash:
    def __init__(self, input_array, leaf_digits=1):
        """
        This class ("Hash") sorts an input array into a hash table & allows it to be search

        :param input_array:
        :param leaf_digits:
        """
        self.hash_dictionary = {}
        self.leaf_digits = leaf_digits
        self.separator = 10 ** leaf_digits

        # Hash Sort
        try:
            input_array.sort()
            for e in input_array:
                # if e is part of the base/0 stem
                if e >= self.separator or e <= -self.separator:
                    if int(str(e)[0:-leaf_digits]) in self.hash_dictionary:
                        if e < 0:
                            self.hash_dictionary[int(str(e)[0:-leaf_digits])].append(int(str(e)[-leaf_digits:]))
                        else:
                            self.hash_dictionary[int(str(e)[0:-leaf_digits])].append(int(str(e)[-leaf_digits:]))
                    else:
                        if e < 0:
                            self.hash_dictionary[int(str(e)[0:-leaf_digits])] = [int(str(e)[-leaf_digits:])]
                        else:
                            self.hash_dictionary[int(str(e)[0:-leaf_digits])] = [int(str(e)[-leaf_digits:])]
                else:
                    if 0 in self.hash_dictionary:
                        self.hash_dictionary[0].append(e)
                    else:
                        self.hash_dictionary[0] = [int(e)]

        except ValueError as e:
            print("Error: only integers are allowed")

    def search(self, value):
        if isinstance(value, int):
            # if value is NOT part of the base/0 stem
            if value >= self.separator or value <= -self.separator:
                # if the starting digits are the same (the hash_dictionary will contain them as a key)
                if int(str(value)[0:-self.leaf_digits]) in self.hash_dictionary:
                    # if self.hash_dictionary[int(str(value)[0:-self.leaf_digits])].__contains__(value):
                    # if the ending digits are the same
                    #   (the hash_dictionary will contain them as part of a value
                    #   (that is a list))
                    if self.hash_dictionary[int(str(value)[0:-self.leaf_digits])].__contains__(
                            int(str(value)[-self.leaf_digits:])):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if 0 in self.hash_dictionary:
                    print(self.hash_dictionary[0])
                    if self.hash_dictionary[0].__contains__(
                            int(str(value)[-self.leaf_digits:])):
                        return True
                else:
                    return False
        else:
            print("Error: only integers are allowed")
            return False

    def print(self):
        for key, value in self.hash_dictionary.items():
            print(f"{key:8} | {value}")


# --- MAIN ---

# Create Hash Table
arr = [
    36, 29, 31, 125, 139, 131, 115, 105, 111, 40, 119, 47, 105,
    57, 122, 109, 124, 115, 43, 120, 43, 27, 27, 32, 61, 37,
    127, 29, 113, 121, 58, 114, 126, 53, 114, 96, 12, 127, 28,
    42, 39, 113, 42, 18, 44, 18, 28, 48, 125, 107, 114, 34, 33,
    45, 120, 30, 127, 31, 116, 146, 58, 109, 23, 105, 63, 27,
    44, 105, 99, 41, 128, 121, 116, 125, 118, 44, 37, 113, 124,
    37, 48, 127, 25, 109, 7, 31, 141, 46, 13, 27, 43, 117, 116,
    27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118, 117, 38,
    27, 106, 33, 117, 116, 132, 104, 123, 35, 113, 122, 42, 117,
    119, 32, 61, 37, 127, 29, 113, 121, 58, 114, 126, 53, 114, 96,
    -22, -444, 443, 0, 0
]
a = Hash(arr)
print(arr)
print()
print(a.hash_dictionary)
print()

# Search Hash Table
print(a.search(124))  # exists
print(a.search(22))  # does not exist
print(a.search(22.5))  # cannot be searched for
print(a.search("a"))  # cannot be searched for
print()

# Print Hash Table
a.print()
print()



