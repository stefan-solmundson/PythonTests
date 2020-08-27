'''
To run a unit test navigate to the folder that contains both the
'app' folder AND 'test' package (folder)

    and type:
    python -m unittest discover

    OR

    In pycharm rmb on the folder & run it
'''

import unittest

from double_linked_list_neighbours.app.doubly_linked_list import DoublyLinkedList

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

