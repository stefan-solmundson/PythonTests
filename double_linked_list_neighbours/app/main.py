from double_linked_list_neighbours.app.doubly_linked_list import DoublyLinkedList


def main():
    # View the test document if you want to see how this class works in more detail
    main_street = DoublyLinkedList()
    main_street.add_node("Nicola")
    print(main_street.delete_node_at_index(1))

    main_street.add_node("James")
    main_street.add_node("Craig")
    main_street.add_node("Riley")
    main_street.add_node("Danae")

    main_street.insert_node_at_index("bob", 22)

    print(main_street.size)
    print(main_street)
    print()

    print(main_street.first.name)
    print(main_street.last.name)
    print(main_street.delete_node_at_index(5))
    print()

    print(main_street.size)
    print(main_street)

    import os
    print(os.path.abspath(__file__))


if __name__ == '__main__':
    main()
