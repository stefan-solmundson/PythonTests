from double_linked_list_neighbours.app.street import Street


def main():
    main_street = Street()
    main_street.add_neighbour("Nicola")
    print(main_street.remove_neighbour(1))

    main_street.add_neighbour("James")
    main_street.add_neighbour("Craig")
    main_street.add_neighbour("Riley")
    main_street.add_neighbour("Danae")

    print(main_street.size)
    print(main_street)
    print()

    print(main_street.first.name)
    print(main_street.last.name)
    print(main_street.remove_neighbour(5))
    print()

    print(main_street.size)
    print(main_street)


if __name__ == '__main__':
    main()
