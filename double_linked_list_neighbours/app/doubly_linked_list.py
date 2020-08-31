from double_linked_list_neighbours.app.doubly_linked_node import DoublyLinkedNode


class DoublyLinkedList:
    def __init__(self):
        self.__first = None
        self.__count = 0
        self.__last = None

    def is_empty(self):
        return self.__first is None

    # read only properties
    @property
    def size(self):
        return self.__count

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    def add_node(self, name):
        if self.is_empty():
            self.__first = DoublyLinkedNode(None, name, None)
            self.__last = self.__first
        else:
            current = self.__first
            while current.next is not None:
                current = current.next
            current.next = DoublyLinkedNode(current, name, None)
            self.__last = current.next
        self.__count += 1

    def insert_node_after(self, name, other_node_name):
        # TODO: implement this
        temp = None

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
    def insert_node_at_index(self, name, index_1_based: int):
        if not (1 <= index_1_based <= self.size+1):
            return False

        # TODO: what if inserting at first location?
        # This isn't possible... :)
        # TODO: what if inserting at last location?

        # insert at 1
        # insert at 3 when 3 is the last element

        # if index_1_based is 1:
        #     self.__first.previous = DoublyLinkedNode(None, name, self.__first)
        #     self.__first = self.__first.previous
        # else:
        previous_node = None
        insert_location_node = self.__first
        for i in range(1, index_1_based):
            if insert_location_node.next is None:  # if navigating to the specified node is impossible
                return False

            previous_node = insert_location_node
            insert_location_node = insert_location_node.next

        if index_1_based is 1:
            self.__first.previous = DoublyLinkedNode(None, name, self.__first)
            self.__first = self.__first.previous

        elif index_1_based is self.__size+1:
            insert_location_node.previous = DoublyLinkedNode(previous_node, name, insert_location_node)

        else:
            previous_node.next = insert_location_node.previous = DoublyLinkedNode(
                previous_node,
                name,
                insert_location_node
            )

        self.__count += 1
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

        self.__count -= 1
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