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

        def add_loop(x, value):
            if value < x.value:
                if x.left is None:
                    temp_node = Node(value)
                    temp_node.parent = x
                    x.left = temp_node
                    # debug
                    # print("{} has been placed on the left below {}".format(x.left.value, x.value))
                else:
                    add_loop(x.left, value)
            elif value > x.value:
                if x.right is None:
                    temp_node = Node(value)
                    temp_node.parent = x
                    x.right = temp_node
                    # debug
                    # print("{} has been placed on the right below {}".format(x.right.value, x.value))
                else:
                    add_loop(x.right, value)
            elif value is x.value:
                print("Error: no 2 nodes in a binary tree can have the same value.")
            else:
                print("Error: the given value in not valid.")

        add_loop(self.node, value)

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
        class TreeList():
            def __init__(self):
                self.list = [[None]]
                self.longest_str = 0

        tree1 = TreeList()
        base_node = self.node

        # debug
        # print(base_node.value)
        # print("-layer")
        # print(base_node.left.value)
        # print(base_node.right.value)
        # print("-layer")
        # print(base_node.left.left.value)
        # # print(base_node.left.right.value) # None
        # print(base_node.left.right is None)
        # print("-same layer")
        # # print(base_node.right.left.value) # None
        # print(base_node.right.right.value)

        '''
        This loops through the binary tree (made of triply linked nodes) & constructs base_node pyramid-shaped-list
        To calculate the position of the next tree-element based on the current tree-element do the following:
        current-tree-element = a,b
        next-tree-element = c,d
        a+1, b*2 + if_right*1
        '''
        def print_loop(current_node, tree, row=0, column=0):
            if len(str(current_node.value)) > tree.longest_str:
                tree.longest_str = len(str(current_node.value))
            tree.list[row][column] = current_node.value

            # debug
            # print(tree.list)
            # print("- Node Added.    tree[{}][{}] will be {}".format(row, column, current_node.value))

            # IF the end of the branch has NOT been reached
            if (current_node.left != None) | (current_node.right != None):

                # IF the pyramid has too few rows to store the node
                if (len(tree.list) - 1) < (row + 1):
                    tree.list.append([None for x in range(2 ** (row + 1))])
                    # print("- Row Added.")

                if current_node.left is not None:
                    # print(base_node.left.value)
                    print_loop(current_node.left, tree, row + 1, column * 2)
                if current_node.right is not None:
                    # print(base_node.right.value)
                    print_loop(current_node.right, tree, row + 1, column * 2 + 1)

        print_loop(base_node, tree1)
        print()

        # print("len(tree1.list)")
        # print(len(tree1.list))

        no_nodes_last_line = 2 ** (len(tree1.list) - 1)
        # print("no_nodes_last_line")
        # print(no_nodes_last_line)
        # print("no_nodes_last_line - double check")
        # print(len(tree1.list[len(tree1.list) - 1]))

        # print("tree1.longest_str")
        # print(tree1.longest_str)

        last_line_length = no_nodes_last_line * (tree1.longest_str + 1)
        # print("last_line_length")
        # print(last_line_length)

        temp_str = ""
        for row_index, row in enumerate(tree1.list):
            # debug
            # print(row)

            # print("row_index")
            # print(row_index)

            # print("str(int(last_line_length / (2 ** row_index))")
            # print(str(int(last_line_length / (2 ** row_index))))

            for node in row:
                # if node is not None:
                #     temp_str += str(node).center(int(last_line_length / (2 ** row_index)))
                # else:
                #     temp_str += "-".center(int(last_line_length / (2 ** row_index)))
                #     # temp_str += " " * int(last_line_length / (2 ** row_index))
                temp_str += str(node).center(int(last_line_length / (2 ** row_index)))
            temp_str += "\n"

        print(temp_str)


# --- MAIN
ll = BinaryTree(2)

ll.add(1)
ll.add(30)
ll.add(14)
ll.add(38)
ll.add(22)
ll.add(10.1)
ll.add(31)
ll.add(-22)
# ll.add(-114)
# ll.add(-24)
# ll.add(-554)
# ll.add(-46)
# ll.add(-47)
# ll.add(-48)

ll.print()
