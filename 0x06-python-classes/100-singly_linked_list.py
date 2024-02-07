#!/usr/bin/python3
"""Defines a node of a singly linked list and a singly linked list class"""


class Node:
    """Define a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes args for a Node instance

        Args:
            data (int): An integer value
            next_node (data): a Node instance
        """

        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Retrieves data."""
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Retrieves a next_node."""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes a private attribute to None."""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node in a correct sorted list in increasing order"""

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Prints the entire list, one node number by line."""

        list_of_datas = []
        tmp = self.__head
        while tmp is not None:
            list_of_datas.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(list_of_datas))
