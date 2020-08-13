'''
list.append(x) - Adds x to the end of the list.
list.extend(iterable) - Extends the list by appending all the items from the iterable.
list.insert(i, x) - Inserts an item at a given position.
list.remove(x) - Removes the first item from the list whose value is equal to x.
list.pop() - Removes AND Returns the last item in the list.
list.pop([i]) - Removes AND Returns the item at the given position in the list.
list.clear() - Clears the list
list.index(x) - Returns index of the first item whose value is equal to x.
list.index(x[, start[, end]]) - Returns index of the first item whose value is equal to x.
list.count(x) - Returns the number of times x appears in the list.
list.sort(key=None, reverse=False) - ...
list.reverse() - ...
'''

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
# 2 1 0

a.insert(2, -1)
a.append(333)
print(a)
# [66.25, 333, -1, 333, 1, 1234.5, 333]

print(a.index(333))
# 1

print(a.remove(333))
a
# [66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print(a)
# [333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print(a)
# [-1, 1, 66.25, 333, 333, 1234.5]

print(a.pop())
# 1234.5

print(a)
# [-1, 1, 66.25, 333, 333]

# --- Transposing a Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

"""
look at the brackets to see where the loops happen
First: i is defined as 0
Thus: row[0] is accessed from matrix
matrix1 kind of acts like range(3)
-
i - the element in transposed1
range(4) - the empty list (of length 4) that is being filled
"""
transposed1 = [[element[i] for element in matrix] for i in range(4)]
print(transposed1)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed2 = []
for i in range(4):
    transposed2.append([row[i] for row in matrix])
print(transposed2)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# --- Delete
a = [1, 3, 10, 45, 6, 50]
del a[2:4]
print(a)
# [1, 3, 6, 50]
