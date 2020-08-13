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
        if self.node.value > value:
            if self.node.left is None:
                temp_node = Node(value)
                self.node.left = temp_node
                temp_node.parent = self.node
            else:
                self.add(self.node.left, value)
        elif self.node.value < value:
            if self.node.right is None:
                temp_node = Node(value)
                self.node.right = temp_node
                temp_node.parent = self.node
            else:
                self.add(self.node.right, value)
        elif value is self.node.value:
            print("Error: no 2 nodes in a binary tree can have the same value.")
        else:
            print("Error: the given value in not valid.")

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

    def ex_print(self):
        print_list = []

        print(self.node)

        def print(self):
            # tabs_count = 0
            # print("\t" * tabs_count)
            # check the number of branches
            # node.left is directly below, node.right is below + a tab
            print_list.append(str(self.node.value))
            if self.node.left is None:
                pass
            else:
                self.print(self.node.left)
            if self.node.right is None:
                pass
            else:
                # add tabs to all of the parents
                print_list.
                self.print(self.node.right)
            # elif value is self.node.value:
            #     print("Error: no 2 nodes in a binary tree can have the same value.")
            # else:
            #     print("Error: the given value in not valid.")

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


# insert node inbetween 2 other nodes

#  --- BODY

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

# Create the Link list object, this REQUIRES the root node
ll = BinaryTree(2)

ll.add(1)
ll.add(2)
ll.add(3)

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
