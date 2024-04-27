""" Defines a generic abstract list with the usual methods. """

__author__ = 'Maria Garcia de la Banda, modified by Brendon Taylor, Graeme Gange, and Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from abc import ABC, abstractmethod
from typing import Generic, TypeVar
T = TypeVar('T')

class List(ABC, Generic[T]):
    """ Abstract class for a generic List. """

    def __init__(self) -> None:
        """ Initialises the length of an exmpty list to be 0. """
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the value of the element at position index to be item
        :pre: index is 0 <= index < len(self)
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index
        :pre: index is 0 <= index < len(self)
        """
        pass

    def __len__(self) -> int:
        """ Returns the length of the list
        :complexity: O(1)
        """
        return self.length

    @abstractmethod
    def is_full(self) -> bool:
        """ Returns True iff the list is full
        """
        pass

    def is_empty(self) -> bool:
        """ Returns True iff the list is empty
        :complexity: O(1)
        """
        return len(self) == 0

    def clear(self):
        """ Sets the list back to empty
        :complexity: O(1)
        """
        self.length = 0

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        """ Moves self[j] to self[j+1] if j>=index, sets self[index]=item
        :pre: index is 0 <= index <= len(self)
        """
        pass

    def append(self, item: T) -> None:
        """ Adds the item to the end of the list; the rest is unchanged.
        :see: #insert(index: int, item: T)
        """
        self.insert(len(self), item)

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """Moved self[j+1] to self[j] if j>index & returns old self[index]
        :pre: index is 0 <= index < len(self)
        """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item
        :raises ValueError: if item not in the list
        """
        pass

    def remove(self, item: T) -> None:
        """ Removes the first occurrence of the item from the list
        :raises ValueError: if item not in the list
        :see: #index(item: T) and #delete_at_index(index: int)
        """
        index = self.index(item)
        self.delete_at_index(index)

    def __str__(self) -> str:
        """ Converts the list into a string, first to last
        :complexity: O(len(self) * M), M is the size of biggest item
        """
        result = '['
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i]) if type(self[i]) != str else "'{0}'".format(self[i])
        result += ']'
        return result