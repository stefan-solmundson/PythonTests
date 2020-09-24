'''
# IN SHORT
add context.py
containing:
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    import app

in each test change the class imports
from:
    from doubly_linked_list_neighbours.app.doubly_linked_list import DoublyLinkedList
to:
    # temp fix
    from .context import app
    from app import *  # does NOT work
    from app.doubly_linked_list import DoublyLinkedList
    # END temp fix

in app change the imports
from:
    from doubly_linked_list_neighbours.app.doubly_linked_node import DoublyLinkedNode
to:
    from app.doubly_linked_node import DoublyLinkedNode

---

# EXTRA
basically none of the imports work normally because
you haven't installed your app folder as a package through pip
you can do this manually using:
    pip install --editable <path/to/package>
this allows your newly edited code to work

Note: pip installable packages are official,
    I dunno how to create these,
    until I have experience don't bother investigating,
    just use this hack
    OR
    add a comment saying to run in the readme.md:
        pip install --editable <path/to/package>

Note: this installs this to your global installation an has issue with virtual environments
        * extra: if you want to test using virtual environments use .venv, import pytest, pip, tox
        * this explains how: https://docs.pytest.org/en/latest/goodpractices.html#tox
        * it doesn't actually explain how, do NOT bother with virtual env. testing this guide sucks

Python Packaging User Guide: https://packaging.python.org/
'''