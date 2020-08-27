'''
To run a unit test navigate to the folder that contains both the
'app' folder AND 'test' package (folder)

    and type:
    python -m unittest discover

    OR

    In pycharm rmb on the folder & run it
'''

import unittest

from double_linked_list_neighbours.app.street import Street

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

    def test_class_most(self):
        s = Street()
        
        with self.subTest("Checking a blank list"):
            self.assertEqual(s.size, 0)
            self.assertEqual(s.is_empty(), True)
            # if self.details is True:
            #     print(s)
            #     print()

        with self.subTest("Trying to removing an item from a blank list"):
            self.assertEqual(s.size, 0)
            self.assertEqual(s.remove_neighbour(0), False)
            self.assertEqual(s.remove_neighbour(1), False)

        with self.subTest("Adding an item"):
            s.add_neighbour("Bob")
            self.assertEqual(s.size, 1)

        with self.subTest("Removing the only item from a list of length 1"):
            self.assertEqual(s.remove_neighbour(1), True)
            self.assertEqual(s.size, 0)

        with self.subTest("Adding 2 Items & __str__"):
            s.add_neighbour("Bob")
            s.add_neighbour("Tom")
            s.add_neighbour("Jane")
            s.add_neighbour("Ray")
            s.add_neighbour("Josh")
            self.assertEqual(s.size, 5)
            self.assertEqual(str(s), "Bob\nTom\nJane\nRay\nJosh")

        with self.subTest("Removing a middle item"):
            s.remove_neighbour(3)
            self.assertEqual(s.size, 4)
            self.assertEqual(str(s), "Bob\nTom\nRay\nJosh")

        with self.subTest("Removing out of index items"):
            self.assertEqual(s.remove_neighbour(10), False)
            self.assertEqual(s.remove_neighbour(-5), False)

        with self.subTest("Removing last item"):
            s.remove_neighbour(4)
            self.assertEqual(s.size, 3)
            self.assertEqual(str(s), "Bob\nTom\nRay")

        with self.subTest("Removing first item"):
            s.remove_neighbour(1)
            self.assertEqual(s.size, 2)
            self.assertEqual(str(s), "Tom\nRay")

