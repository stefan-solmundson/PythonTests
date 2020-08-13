# delete node & reorganise


def delete_node(x):
    if x.leftnode is not None and x.rightnode is not None:  # there are 2 lower nodes
        x.value = x.rightnode.leftnode.value
        delete_node(x.rightnode.leftnode)
    else:
        if x.leftnode is not None:
            x = x.leftnode
        if x.rightnode is not None:
            x = x.rightnode
        x.parent.delete_child(x)


# if self.leftnode is not None and self.rightnode is not None:  # there are 2 lower nodes
#     self.value = self.rightnode.leftnode.value
#     # reorganise
#     check if there are 2 lower nodes (rightnode.leftnode)
# else:
#     if leftnode != none:
#
#
#     leftnode.parent = parent.parent





