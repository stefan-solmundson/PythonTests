# delete node & reorganise


# if self.left is not None and self.right is not None:  # there are 2 lower nodes
#     self.value = self.right.left.value
#     # reorganise
#     check if there are 2 lower nodes (right.left)
# else:
#     if left != none:
#
#
#     left.parent = parent.parent

# ---

# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# unit tests : https://github.com/Sandyman/guess-the-number


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self, value):
        self.node = Node(value)

    def add(self, value):

        def add2(x, value):
            if x.value > value:
                if x.left is None:
                    temp_node = Node(value)
                    temp_node.parent = x
                    x.left = temp_node
                else:
                    add2(x.left, value)
            elif x.value < value:
                if x.right is None:
                    temp_node = Node(value)
                    temp_node.parent = x
                    x.right = temp_node
                else:
                    add2(x.right, value)
            elif value is x.value:
                print("Error: no 2 nodes in a binary tree can have the same value.")
            else:
                print("Error: the given value in not valid.")

        add2(self.node, value)

    def search(self, value):
        if self.node.value > value:
            if self.node.left is None:
                print("Not found")
            else:
                self.add(self.node.left, value)
        elif self.node.value < value:
            if self.node.right is None:
                print("Not found")
            else:
                self.add(self.node.right, value)
        elif value is self.node.value:
            return self.node
        else:
            print("Error: the given value in not valid.")

    def delete_node(self, value):
        x = self.search(self, value)
        if x.left is not None and x.right is not None:  # if there are 2 lower nodes
            x.value = x.right.left.value
            self.delete_node(x.right.left)
        elif x.left is not None:
            x = x.left
        elif x.right is not None:
            x = x.right
        else:
            x.parent.delete_child(x.value)

    def delete_child(self, value):
        if self.node.left.value is value:
            self.node.left = None
        elif self.node.right.value is value:
            self.node.right = None
        else:
            print("Error: a node with the given value does not exist.")

    def print(self):
        # list = [[None for x in range(20)] for y in range(5)]
        list = [[None]]

        a = self.node
        # print(a.value)
        # print("-layer")
        # print(a.left.value)
        # print(a.right.value)
        # print("-layer")
        # print(a.left.left.value)
        # # print(a.left.right.value) # None
        # print(a.left.right is None)
        # print("-same layer")
        # # print(a.right.left.value) # None
        # print(a.right.right.value)

        import pprint

        def pp(a, left=0, right=0):
            print("list[{}][{}] = tree[{}][{}] will be {}".format(left+right, right, left, right, a.value))
            list[left+right][right] = a.value

            pprint.pprint(list, width=100, compact=True)

            if a.left is not None or a.right is not None:
                # print(len(list))
                # print(left + right + 1)
                # print("test")
                if (len(list) - 1) < (left + right + 1):
                    list.append([None for x in range(2 ** (left + right + 1))])
                    pprint.pprint(list, width=100, compact=True)
                # print("left: {}".format(left))
                # print("right: {}".format(right))
                if a.left is not None:
                    # print(a.left.value)
                    pp(a.left, left+1, right)
                if a.right is not None:
                    # print(a.right.value)
                    pp(a.right, left, right+1)

        pp(a)

        '''
        I've run into the issue now where I can't tell the path that has been taken
        I simply know a node has 4 losses & 3 wins, 
        but I do not know the order of these,
        so I cannot determine where to place it in the tree structure
        
        a list will be constructed rather that right & left, it will be a list, 
        e.g. [0,1,1,0,1] this represents left, right, right, left right
        now we know exactly where in the tree the thing is, 
        we just need to convert this tree notation into list notation,
        which is NOT a trivial task
        the length of this list is important
        *if it is 5 long as above;
        2**(length-row)
        2**(5-row)
        a row 1 win moves the list position 2**(5-1) right
        a row 2 win moves the list position 2**(5-2) right
        a row 3 win moves the list position 2**(5-3) right
        a row 4 win moves the list position 2**(5-4) right
        a row 5 win moves the list position 2**(5-5) right
        ->
            a row 1 win moves the list position 2**(4) right
            a row 2 win moves the list position 2**(3) right
            a row 3 win moves the list position 2**(2) right
            a row 4 win moves the list position 2**(1) right
            a row 5 win moves the list position 2**(0) right
            ->
                a row 1 win moves the list position 16 right
                a row 2 win moves the list position 8 right
                a row 3 win moves the list position 4 right
                a row 4 win moves the list position 2 right
                a row 5 win moves the list position 1 right
                ---
                SO 
                list row = 5
                list column = 16*0 + 8*1 + 4*1 + 2*0 + 1*1
                ->
                    list row = 5
                    list column = 8 + 4 + 1
                    ->
                        list row = 5
                        list column = 13
                        ---
                        SO
                        T[0,1,1,0,1] = L[5,13]
                        T[x,x,x,x,x] = L[len(T),
                                                (2**(len(T) - (x.column + 1)) * x.bool +
                                                (2**(len(T) - (x.column + 1)) * x.bool +
                                                (2**(len(T) - (x.column + 1)) * x.bool +
                                                (2**(len(T) - (x.column + 1)) * x.bool +
                                                etc.
                                        ]
        
        # It seems the only solution is recursion, 
        # go left as far as possible keeping track of the present node 
        # & the last node that allowed a branch to the right
        # record the 
        '''


        # # left + right = row
        # # right = column
        # def print2(x, left=0, right=0):
        #     # # debug
        #     # print(x)
        #     # print(x.value)
        #     # print(x.left)
        #     # print(x.right)
        #
        #     # ---
        #     print("len(list): {0}".format(len(list)))
        #     # print(len(list[]))
        #
        #     print("-array")
        #
        #     for i in list:
        #         print("{0}, length: {1}".format(i, len(i)))
        #         for j in i:
        #             print("\t {0}".format(j))
        #     # ---
        #
        #     # useless
        #     # print(len([None] * (left + right) * (left + right)))
        #
        #     # repr(list)
        #
        #     # add self
        #     list[left][right] = x.value
        #
        #     # extend list
        #     if x.left is not None or x.right is not None:
        #         if len(list) < left + right:
        #         list.append([None] * (left + right + 1) * (left + right + 1))
        #         # list.append([None] * 4)
        #         print("-d1")
        #         if x.left is not None:
        #             # print(x.left + (6 - len(str(x.left.value))) * " ")
        #             print2(x.left, left+1, right)
        #             print("-d2")
        #         if x.right is not None:
        #             # print(x.right + (6 - len(str(x.left.value))) * " ")
        #             print2(x.right, left, right+1)
        #             print("-d3")
        #     print("-a")
        #
        # print2(self.node)

        # def print(self):
        #     list = [[None]]
        #
        #     # left + right = row
        #     # right = column
        #     def print2(x, left=0, right=0):
        #         # # debug
        #         # print(x)
        #         # print(x.value)
        #         # print(x.left)
        #         # print(x.right)
        #
        #         # ---
        #         print("len(list): {0}".format(len(list)))
        #         # print(len(list[]))
        #
        #         print("-array")
        #
        #         for i in list:
        #             print("{0}, length: {1}".format(i, len(i)))
        #             for j in i:
        #                 print("\t {0}".format(j))
        #         # ---
        #
        #         # useless
        #         # print(len([None] * (left + right) * (left + right)))
        #
        #         # repr(list)
        #
        #         # add self
        #         list[left][right] = x.value
        #
        #         # extend list
        #         if x.left is not None or x.right is not None:
        #             if len(list) < left + right:
        #                 list.append([None] * (left + right + 1) * (left + right + 1))
        #             # list.append([None] * 4)
        #             print("-d1")
        #             if x.left is not None:
        #                 # print(x.left + (6 - len(str(x.left.value))) * " ")
        #                 print2(x.left, left + 1, right)
        #                 print("-d2")
        #             if x.right is not None:
        #                 # print(x.right + (6 - len(str(x.left.value))) * " ")
        #                 print2(x.right, left, right + 1)
        #                 print("-d3")
        #         print("-a")
        #
        #     print2(self.node)



        # # start
        # print(self.node.value)
        # # first row
        # print(self.node.left.value)
        # print(self.node.right.value)
        # # second row


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# Create the Link list object, this REQUIRES the root node
ll = BinaryTree(2)

ll.add(1)
# ll.add(2)
ll.add(3)
# print(ll.node.value)
ll.add(5)
ll.add(0)
ll.add(8)
ll.add(-22)
ll.add(-44)

ll.print()

# list = []
# left = 0
# right = 0
# list.append([None] * (left + right) * (left + right))
# left = 2
# right = 0
# list.append([None] * (left + right) * (left + right))
# print(len(list))
# print(len(list[0]))
# print(len(list[1]))
# print(list[1])









# # Link Nodes in Series
# e1.left = e2
# e2.left = e3
# e3.left = e4
# e4.left = e5

# ll.print()
#
# print("-")
#
# e0 = Node("Origin")
# ll.insert_as_first(e0)
# ll.print()
#
# print("-")
#
# eI = Node("Insert")
# ll.insert_after(eI, "Mon")
# ll.print()
#
# print("-")
#
# eI2 = Node("Insert Fail")
# ll.insert_after(eI2, "Mo")
# ll.print()
#
# # !!! Add the delete function!!!

from array import *

# list = [[5], [2, 2], [3, 3, 3]]
#
# print(list[0][0])
# print(list[1][0])
# if len(list) < 4:
#     print("doesn't exist")
# else:
#     print(list[3])


# def print(self):
#     current_node = self.node
#     while current_node is not None:
#         print(current_node.value)
#         # this is kind of dangerous, as this class does NOT know that .next_node is a property of the selected item
#         current_node = current_node.next_node
#
# def insert_as_first(self, node):
#     current_first_node = self.node
#     self.node = node
#     node.next_node = current_first_node
#
# # !!! This does not say if it fails to find the NODE!
# def find(self, element_value):
#     current_node = self.node
#     while current_node.value is not element_value or None:
#         # this is kind of dangerous, as this class does NOT know that .next_node is a property of the selected item
#         if current_node.next_node.next_node is None:
#             print("No element matches the specified search.")
#             return False
#         current_node = current_node.next_node
#     return current_node
#
# def insert_after(self, node, element_value):
#     # search for a match
#     current_node = self.find(element_value)
#     node.next_node = current_node.next_node
#     current_node.next_node = node

# def ex_print(self):
    #     print_list = []
    #
    #     print(self.node)
    #
    #     def print(self):
    #         # tabs_count = 0
    #         # print("\t" * tabs_count)
    #         # check the number of branches
    #         # node.left is directly below, node.right is below + a tab
    #         print_list.append(str(self.node.value))
    #         if self.node.left is None:
    #             pass
    #         else:
    #             self.print(self.node.left)
    #         if self.node.right is None:
    #             pass
    #         else:
    #             # add tabs to all of the parents
    #             print_list.
    #             self.print(self.node.right)
    #         # elif value is self.node.value:
    #         #     print("Error: no 2 nodes in a binary tree can have the same value.")
    #         # else:
    #         #     print("Error: the given value in not valid.")