""" Linked-node based implementation of List ADT. """
from data_structures.node import Node
import data_structures.node as node
from data_structures.abstract_list import List, T
from typing import Generic

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class LinkedList(List[T]):
    """ List ADT implemented with linked nodes. """
    def __init__(self, dummy_capacity=1) -> None:
        """ Linked-list object initialiser. """
        List.__init__(self) # Could use super(LinkedList, self).__init__() instead
        self.head = None

    def clear(self):
        """ Clear the list. """
        # first call clear() for the base class
        List.clear(self)
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        node = self._get_node_at_index(index)
        node.item = item

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        node_at_index = self._get_node_at_index(index)
        return node_at_index.item

    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        return node.index(self.head, item)

    def _get_node_at_index(self, index: int) -> Node[T]:
        """ Get node object at a given position. """
        if 0 <= index and index < len(self):
            return node.get_node_at_index(self.head, index)
        else:
            raise ValueError('Index out of bounds')

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        if self.is_empty():
            raise Exception("Can't delete from empty list")
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")            

        # Delete from front
        if index == 0:
            item = self.head.item
            self.head = self.head.next
        # Delete in the middle
        else:
            previous_node = self._get_node_at_index(index - 1)
            item = previous_node.next.item
            previous_node.next = previous_node.next.next

        self.length -= 1
        return item

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        new_node = Node(item)

        # Inserting at the head of the list
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        # Inserting in the middle
        else:
            previous_node = self._get_node_at_index(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
        
        self.length += 1

    def append(self, item: T) -> None:
        """ Insert an item at a given position. """
        self.head = node.append(self.head, item)
    
    def __iter__(self):
        """ Magic method. Creates and returns an iterator for the list. """
        return LinkedListIterator(self.head)


class LinkedListIterator(Generic[T]):
    """ A full-blown iterator for class LinkedList.

        Attributes:
            current (Node[T]): the node whose item will be returned next
    """
    def __init__(self, node: Node[T]) -> None:
        """ Initialises self.current to the node given as input. """
        self.current = node

    def __iter__(self):
        """ Returns itself, as required to be iterable. """
        return self

    def __next__(self) -> T:
        """ Returns the current item and moves to the next node.
            :raises StopIteration: if the current item does not exist
        """
        if self.current is not None:
            item = self.current.item
            self.current = self.current.next
            return item
        else:
            raise StopIteration