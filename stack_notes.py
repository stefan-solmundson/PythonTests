# https://docs.python.org/3.8/tutorial/datastructures.html#using-lists-as-stacks
# meh : https://www.geeksforgeeks.org/stack-in-python/

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)
# [3, 4, 5, 6, 7]

print(stack.pop())
# 7

print(stack)
# [3, 4, 5, 6]

print(stack.pop())
# 6

print(stack.pop())
# 5

print(stack)
# [3, 4]
