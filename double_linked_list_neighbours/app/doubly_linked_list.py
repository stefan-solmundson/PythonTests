from double_linked_list_neighbours.app.doubly_linked_node import DoublyLinkedNode


class DoublyLinkedList:
    def __init__(self):
        self.__first = None
        self.__size = 0
        self.__last = None

    def is_empty(self):
        return self.__first is None

    # read only properties
    @property
    def size(self):
        return self.__size

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    def add_node(self, name):
        # if self.is_empty():
        if self.__size == 0:
            self.__first = self.__last = DoublyLinkedNode(None, name, None)
        else:
            current = self.__first
            while current.next is not None:
                current = current.next
            current.next = DoublyLinkedNode(current, name, None)
            self.__last = current.next
        self.__size += 1

    def insert_node_after(self, name, other_node_name):
        if self.__size == 0:
            return False

        current_node = self.__first
        for i in range(1, self.__size+1):
            if current_node.name is other_node_name:
                # print("{0}: found".format(other_node_name))
                current_node.next = current_node.next.previous = DoublyLinkedNode(current_node, name, current_node.next)
                self.__size += 1
                return True

            if current_node.next is None:
                # print("{0}: not found".format(other_node_name))
                return False
            else:
                current_node = current_node.next

    def delete_node(self, name):
        if self.__size == 0:
            return False

        if self.__first.name == name:
            if self.size == 1:
                self.__first = self.__last = None

                self.__size -= 1
                return True
            else:
                self.__first = self.__first.next
                self.__first.previous = None

                self.__size -= 1
                return True

        if self.__last.name == name:
            self.__last = self.__last.previous
            self.__last.next = None

            self.__size -= 1
            return True

        current_node = self.__first
        for i in range(1, self.__size+1):
            if current_node.name is name:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                self.__size -= 1
                return True

            if current_node.next is None:
                # print("{0}: not found".format(name))
                return False
            else:
                current_node = current_node.next

    def redefine_node(self, old_name, new_name):
        if self.__size == 0:
            return False

        current_node = self.__first
        for i in range(1, self.__size+1):
            # print(current_node.name)

            if current_node.name is old_name:
                # print("{0}: found".format(other_node_name))
                '''
                current_node = DoublyLinkedNode(current_node.previous, new_name, current_node.next)
                
                this doesn't work because you can only change the attributes of a referenced
                object, not the object itself
                '''
                if current_node.previous is None:
                    self.__first = DoublyLinkedNode(None, new_name, current_node.next)
                    if current_node.next is None:
                        self.__first = self.__last = DoublyLinkedNode(None, new_name, None)
                    else:
                        current_node.previous.next = current_node.next.previous = DoublyLinkedNode(
                            current_node.previous, new_name, current_node.next)
                elif current_node.next is None:
                    self.__last = DoublyLinkedNode(current_node.previous, new_name, None)

                return True

            if current_node.next is None:
                # print("{0}: not found".format(other_node_name))
                return False
            else:
                current_node = current_node.next

    # TODO: stick this somewhere that makes sense
    '''
    Annotations:
    
    Type Hints:
        This does work, but IDEs don't support it
        # def insert_node_at_index(self, name, index: "The list's index is 1-based"):  
    
    Generic Annotations:
        IDEs do NOT support generic annotation in their parameter hints,
         generic annotation are more like metadata & can be manually accessed in Python
        def insert_node_at_index(self, name, index_1_based: int):
    
    source : https://realpython.com/lessons/type-hinting/
    source : https://www.python.org/dev/peps/pep-3107/#syntax
    '''
    def insert_node_at_index(self, name: str, index_1_based: int):
        if not (1 <= index_1_based <= self.__size+1):
            return False

        if self.__size == 0:
            self.__first = self.__last = DoublyLinkedNode(None, name, None)

        elif index_1_based is 1:
            self.__first.previous = DoublyLinkedNode(None, name, self.__first)
            self.__first = self.__first.previous

        elif index_1_based == self.__size+1:
            self.__last.next = DoublyLinkedNode(self.__last, name, None)
            self.__last = self.__last.next

        else:
            insert_location_node = self.__first
            for i in range(1, index_1_based):
                if insert_location_node.next is None:  # if navigating to the specified node is impossible
                    return False

                insert_location_node.previous = insert_location_node = insert_location_node.next

            insert_location_node.previous.next = DoublyLinkedNode(insert_location_node.previous, name, insert_location_node)

        self.__size += 1
        return True

    def delete_node_at_index(self, index):
        if not (1 <= index <= self.size):
            return False

        previous_node = None
        terminating_node = self.__first
        for i in range(1, index):  # navigating to the specified node
            if terminating_node.next is None:  # if navigating to the specified node is impossible
                return False

            previous_node = terminating_node
            terminating_node = terminating_node.next

        if index == 1:
            self.__first = terminating_node.next
            if self.__first is not None:
                self.__first.previous = None

        if index == self.size:
            self.__last = terminating_node.previous
            if self.__last is not None:
                self.__last.next = None

        else:
            terminating_node.next.previous = previous_node
            if previous_node is not None:  # if you are deleting the first node there is no previous node
                previous_node.next = terminating_node.next

        self.__size -= 1
        return True

    # prints out all of the people in the street (in ascending order) (the street has no name)
    def __str__(self):
        current = self.__first
        output = ""

        output += current.name
        while current.next is not None:
            output += "\n"
            output += current.next.name
            current = current.next

        return output