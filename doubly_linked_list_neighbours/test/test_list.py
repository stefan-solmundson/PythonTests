'''
To run a unit test navigate to the folder that contains both the
'app' folder AND 'test' package (folder)

    and type:
    python -m unittest discover

    OR

    In pycharm rmb on the folder & run it
'''

import sys, os

# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))

import unittest

# # temp fix
# from .context import app
# from app import *
# from app.doubly_linked_list import DoublyLinkedList
# # END temp fix

from doubly_linked_list_neighbours.app.doubly_linked_list import DoublyLinkedList
# from app.doubly_linked_list import DoublyLinkedList

# https://docs.python.org/3/library/unittest.html#command-line-interface
# python -m unittest -v
# DOES NOTHING !!!
# WHERE ARE THE EXTRA DETAILS!!!
# https://docs.python.org/3/library/unittest.html#grouping-tests


class TestList(unittest.TestCase):
    # def setUp(self):
    #     # Create a list to be used for all tests
    #     main_street = Street()
    #     main_street.add_neighbour("Nicola")
    #     main_street.add_neighbour("James")
    #     main_street.add_neighbour("Craig")
    #     main_street.add_neighbour("Riley")
    #     main_street.add_neighbour("Danae")

    def test_entire_class(self):
        s = DoublyLinkedList()

        with self.subTest("Checking a blank list"):
            self.assertEqual(s.size, 0)
            self.assertEqual(s.is_empty(), True)
            # print(s)
            # print()

        with self.subTest("Trying to removing an item from a blank list"):
            self.assertEqual(s.size, 0)
            self.assertEqual(s.delete_node_at_index(0), False)
            self.assertEqual(s.delete_node_at_index(1), False)
            # print(s)
            # print()

        with self.subTest("Adding an item"):
            s.add_node("Bob")
            self.assertEqual(s.size, 1)
            # print(s)
            # print()

        with self.subTest("Removing the only item from a list of length 1"):
            self.assertEqual(s.delete_node_at_index(1), True)
            self.assertEqual(s.size, 0)
            # print(s)
            # print()

        with self.subTest("Adding 2 Items & __str__"):
            s.add_node("Bob")
            s.add_node("Tom")
            s.add_node("Jane")
            s.add_node("Ray")
            s.add_node("Josh")
            self.assertEqual(s.size, 5)
            self.assertEqual(str(s), "Bob\nTom\nJane\nRay\nJosh")
            # print(s)
            # print()

        with self.subTest("Removing a middle item"):
            s.delete_node_at_index(3)
            self.assertEqual(s.size, 4)
            self.assertEqual(str(s), "Bob\nTom\nRay\nJosh")
            # print(s)
            # print()

        with self.subTest("Removing out of index items"):
            self.assertEqual(s.delete_node_at_index(10), False)
            self.assertEqual(s.delete_node_at_index(-5), False)
            # print(s)
            # print()

        with self.subTest("Removing last item"):
            s.delete_node_at_index(4)
            self.assertEqual(s.size, 3)
            self.assertEqual(str(s), "Bob\nTom\nRay")
            # print(s)
            # print()

        with self.subTest("Removing first item"):
            s.delete_node_at_index(1)
            self.assertEqual(s.size, 2)
            self.assertEqual(str(s), "Tom\nRay")
            # print(s)
            # print()

    def test_attributes(self):  # name: "Testing attributes & mutability"
        s = DoublyLinkedList()

        with self.subTest("size"):
            self.assertEqual(True, hasattr(DoublyLinkedList, "size"))
            # OR
            # self.assertEqual(True, hasattr(DoublyLinkedList, DoublyLinkedList.size))
            try:
                s.size = 100
            except AttributeError as e:
                pass
                # print(e)
            self.assertNotEqual(s.size, 100)
            self.assertEqual(s.size, 0)

        with self.subTest("first"):
            self.assertEqual(True, hasattr(DoublyLinkedList, "first"))
            try:
                s.first = 100
            except AttributeError as e:
                pass
                # print(e)
            self.assertNotEqual(s.first, 100)
            self.assertEqual(s.first, None)

        with self.subTest("last"):
            self.assertEqual(True, hasattr(DoublyLinkedList, "last"))
            try:
                s.first = 100
            except AttributeError as e:
                pass
                # print(e)
            self.assertNotEqual(s.last, 100)
            self.assertEqual(s.last, None)

    def test_insert_node_at_index(self):
        s = DoublyLinkedList()

        self.assertEqual(s.insert_node_at_index("Ted", -1), False)
        self.assertEqual(s.insert_node_at_index("Ted", 0), False)
        self.assertEqual(s.insert_node_at_index("Ted", 0.5), False)
        self.assertEqual(s.insert_node_at_index("Ted", 3), False)
        self.assertEqual(s.size, 0)

        self.assertEqual(s.insert_node_at_index("Ted", 1), True)
        self.assertEqual(s.size, 1)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_at_index("Gabe", 1), True)
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_at_index("Allen", 2), True)
        self.assertEqual(s.size, 3)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_at_index("Brodie", 4), True)
        self.assertEqual(s.size, 4)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_at_index("Ned", 7), False)

    def test_insert_node_after(self):
        s = DoublyLinkedList()

        s.add_node("Bob")
        s.add_node("Ruth")
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_after("Jane", "Norman"), False)
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_after("Jane", "Bob"), True)
        self.assertEqual(s.size, 3)
        # print(s)
        # print()

        self.assertEqual(s.insert_node_after("Dillon", "Ruth"), True)
        self.assertEqual(s.size, 4)
        # print(s)
        # print()

    def test_redefine_node(self):
        s = DoublyLinkedList()

        self.assertEqual(s.redefine_node("Bob", "Newer Bob"), False)

        s.add_node("Bob")
        self.assertEqual(s.size, 1)
        # print(s)
        # print()

        self.assertEqual(s.redefine_node("Bob", "Newer Bob"), True)
        self.assertEqual(s.size, 1)
        # print(s)
        # print()

        self.assertEqual(s.redefine_node("Newer Bob", "Newest Bob"), True)
        self.assertEqual(s.size, 1)
        # print(s)
        # print()

        s.add_node("Tim")
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

        self.assertEqual(s.redefine_node("Tim", "Jane"), True)
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

    def test_delete_node(self):
        s = DoublyLinkedList()

        # Cannot delete from an empty list
        self.assertEqual(s.delete_node("Bob"), False)

        s.add_node("Bob")
        s.add_node("Jane")
        s.add_node("Cody")
        s.add_node("Ruth")
        self.assertEqual(s.size, 4)
        # print(s)
        # print()

        # Cannot delete using the wrong name
        self.assertEqual(s.delete_node("Wrong Name"), False)

        # Delete First Link
        self.assertEqual(s.delete_node("Bob"), True)
        self.assertEqual(s.size, 3)
        # print(s)
        # print()

        # Delete Middle Link
        self.assertEqual(s.delete_node("Cody"), True)
        self.assertEqual(s.size, 2)
        # print(s)
        # print()

        # Delete Last Link
        self.assertEqual(s.delete_node("Ruth"), True)
        self.assertEqual(s.size, 1)
        # print(s)
        # print()

        # Delete Only Remaining Link
        self.assertEqual(s.delete_node("Jane"), True)
        self.assertEqual(s.size, 0)






