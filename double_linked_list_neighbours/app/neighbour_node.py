class NeighbourNode:
    def __init__(self, _previous, name, _next):
        self.previous = _previous
        self.__name = name
        self.next = _next

    @property
    def name(self):
        return self.__name

    # def __str__(self):
    #     return " Neighbour: " + self.name + ".\n"
