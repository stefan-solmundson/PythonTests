'''
To run a unit test navigate to the folder that contains both the
'app' folder AND 'test' package (folder)

    and type:
    python -m unittest discover

    OR

    In pycharm rmb on the folder & run it
'''

import unittest
from app.stack import Stack
# OR
# from ..app.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        # Create a stack to be used for all tests with a depth of 3
        self.stack = Stack(max_size=3)

    def test_is_empty_returns_true_for_empty_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_full_returns_false_for_empty_stack(self):
        self.assertFalse(self.stack.is_full())

    def test_is_empty_returns_false_if_stack_has_elements(self):
        self.stack.push(3)
        self.assertFalse(self.stack.is_empty())

    def test_is_full_returns_false_if_stack_has_not_reached_capacity(self):
        self.stack.push(5)
        self.assertFalse(self.stack.is_full())

    def test_is_full_returns_true_if_stack_has_reached_capacity(self):
        self.stack.push(4)
        self.stack.push(8)
        self.stack.push(10)
        self.assertTrue(self.stack.is_full())

    def test_pop_should_return_last_element_pushed(self):
        self.stack.push("a")
        self.stack.push("b")
        last_element = self.stack.pop()
        self.assertEqual(last_element, "b")

    def test_elements_popped_in_reverse_order(self):
        data = [1, 2, 3]
        for x in data:
            self.stack.push(x)

        result = []
        for _ in data:
            result.append(self.stack.pop())

        # Compare original array with reverse array
        self.assertEqual(data, result[::-1])

    def test_pop_from_empty_stack_should_raise_exception(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_push_onto_full_stack_should_raise_exception(self):
        self.stack.push(0)
        self.stack.push(3)
        self.stack.push(9)
        with self.assertRaises(IndexError):
            self.stack.push(3)

    def test_peek_from_empty_stack_should_raise_exception(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_peek_should_not_change_the_stack(self):
        self.stack.push(1)
        for _ in range(10):
            # We could do this a million times and it should still work
            self.assertFalse(self.stack.is_empty())
            result = self.stack.peek()
            self.assertEqual(result, 1)
