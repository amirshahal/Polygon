# Jether Energy Python Exercise - Amir Shahal - Oct 20th, 2020, file 3 out of 5 files.
class CircularDoublyLinkedList:
    """A class used to represent a Circular Doubly Linked List with minimal functionality.
    Source: https://www.sanfoundry.com/python-program-implement-circular-doubly-linked-list/
    The following changes were made:
    1. Only required methods are kept.
    2. After every method that changes the typology structure of the list, a call to set_neighbors_related_values()
        is issued for the relevant nodes. This call makes the node update variables which are related to its adjacent
        nodes.

    Attributes
    ----------
    first : object
        The first item in the list.
    """
    def __init__(self):
        """Create an empty Circular Doubly Linked List"""
        self.first = None

    @staticmethod
    def insert_after(ref_node, new_node):
        """Insert a new node after ref_node

        Parameters:
            ref_node : object - the object to insert the new node after.
            new_node : object - the new node to insert.

        Notice:
            1. Since this method changes the linked list topology, it MUST call set_neighbors_related_values() on the
                relevant node.
            2. All methods are in O(1).
        """
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

        new_node.set_neighbors_related_values()

    def insert_at_end(self, new_node):
        """Insert a new node at the end of the list

        Parameters:
            new_node : object - the new node to insert

        Notice:
            Since this method changes the linked list topology, it MUST call set_neighbors_related_values() on the
                relevant node.
        """

        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)

        new_node.set_neighbors_related_values()

    def insert_at_beg(self, new_node):
        """Insert a new node at the beginning of the list

         Parameters:
            new_node : object - the new node to insert

        Notice:
            Since this method uses insert_at_end() method which already calling set_neighbors_related_values() for the
                relevant node, there is no need to call it in this function.
        """
        self.insert_at_end(new_node)
        self.first = new_node

    def remove(self, node):
        """Remove a node from the list.
        Parameters:
            node : object - the node to remove.

        Notice:
            Since this method changes the linked list topology, it MUST call set_neighbors_related_values() on the
                relevant node, which in this case is the next node after the one removed.
        """
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next

        node.next.set_neighbors_related_values()
