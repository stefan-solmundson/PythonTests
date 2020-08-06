# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# unit tests : https://github.com/Sandyman/guess-the-number

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class SLinkedList:
    def __init__(self, node=None):
        self.node = node

    def print(self):
        current_node = self.node
        while current_node is not None:
            print(current_node.value)
            # this is kind of dangerous, as this class does NOT know that .next_node is a property of the selected item
            current_node = current_node.next_node

    def insert_as_first(self, node):
        current_first_node = self.node
        self.node = node
        node.next_node = current_first_node

    # !!! This does not say if it fails to find the NODE!
    def find(self, element_value):
        current_node = self.node
        while current_node.value is not element_value or None:
            # this is kind of dangerous, as this class does NOT know that .next_node is a property of the selected item
            if current_node.next_node.next_node is None:
                print("No element matches the specified search.")
                return False
            current_node = current_node.next_node
        return current_node

    def insert_after(self, node, element_value):
        # search for a match
        current_node = self.find(element_value)
        node.next_node = current_node.next_node
        current_node.next_node = node


# insert node inbetween 2 other nodes

#  --- BODY

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
e5 = Node("Fri")

# Create the Link list object, this REQUIRES the root node
ll = SLinkedList(e1)

# Link Nodes in Series
e1.next_node = e2
e2.next_node = e3
e3.next_node = e4
e4.next_node = e5

ll.print()

print("-")

e0 = Node("Origin")
ll.insert_as_first(e0)
ll.print()

print("-")

eI = Node("Insert")
ll.insert_after(eI, "Mon")
ll.print()

print("-")

eI2 = Node("Insert Fail")
ll.insert_after(eI2, "Mo")
ll.print()

# !!! Add the delete function!!!