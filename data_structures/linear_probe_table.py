""" Hash Table ADT.

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '16/05/2020'
__since__ = '14/05/2020'

from data_structures.referential_array import ArrayR
from typing import TypeVar, Generic, Callable
T = TypeVar('T')

class DeletedItem:
    pass

class LinearProbeTable(Generic[T]):
    """
    Linear Probe Hash Table

    attributes:
        count: number of elements in the hash table
        table: used to represent our table as an internal array
    """
    DEFAULT_TABLE_SIZE = 17

    def __init__(self, hash_fun: Callable[[str, int], int], table_size: int = DEFAULT_TABLE_SIZE) -> None:
        """
        :complexity: O(N) where N is the table_size
        """
        assert(table_size > 0)
        self.hash = hash_fun
        self.count = 0
        self.table = ArrayR(table_size)

    def __getitem__(self, key: str) -> T:
        """
        Find the data associated with a key in our hash table
        :complexity: O(hash) + O(N * comp), where N is the number of elements in the table, comp and hash are the complexity
                     hashing and comparison (usually both linear in the key size).
        :raises: KeyError if key is not in the table
        """
        position = self.hash(key, len(self.table))
        for _ in range(len(self.table)):
            if self.table[position] is None:
                break
            elif self.table[position] is not DeletedItem and self.table[position][0] == key:
                    return self.table[position][1]  # data
            position = (position + 1) % len(self.table)
        raise KeyError('key is not found')

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :complexity: O(hash) + O(N * comp), where N is the number of elements in the table, comp and hash are the complexity
                     hashing and comparison (usually both linear in the key size).
        :raises: KeyError if the hash table is full
        """
        position = self.hash(key, len(self.table))

        potential_pos = None
        for _ in range(self.count):
            # Empty position
            if self.table[position] is None or self.table[position] is DeletedItem:
                if potential_pos is None:
                    potential_pos = position
            # Non-empty position
            elif self.table[position][0] == key:
                self.table[position] = (key, data)  # updating the item
                return
            position = (position + 1) % len(self.table)
        else:
            if potential_pos is None:
                raise KeyError('Table is full')

        self.table[potential_pos] = (key, data)
        self.count += 1
        return

    def __delitem__(self, key: str) -> T:
        """
        Find the data associated with a key in our hash table
        :complexity: O(hash) + O(N * comp), where N is the number of elements in the table, comp and hash are the complexity
                     hashing and comparison (usually both linear in the key size).
        :raises: KeyError if key is not in the table
        """
        position = self.hash(key, len(self.table))
        for _ in range(len(self.table)):
            if self.table[position] is None:
                break
            elif self.table[position] is not DeletedItem and self.table[position][0] == key:
                item = self.table[position]
                self.table[position] = DeletedItem
                self.count -= 1
                return item
            position = (position + 1) % len(self.table)
        raise KeyError('key is not found')

