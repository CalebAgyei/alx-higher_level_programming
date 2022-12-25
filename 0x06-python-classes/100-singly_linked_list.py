#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes node of singly linked list.

        Args:
            @data: Data elements to linked list
            @next_node: Pointer to next data element in linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns private data element."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets private instance of data element to new value."""
        if not isinstance(value, int):
            raise TypeError('data must be an  integer')
        self.__data = value

    @property
    def next_node(self):
        """Returns private instance of pointer to next data element."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets private instance of pointer to next data element to new value."""
        if not isinstance(value, Node) or value != None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
