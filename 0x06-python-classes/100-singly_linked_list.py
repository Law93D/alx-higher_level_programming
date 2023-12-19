#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""



class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initializes the Node instance."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position."""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
