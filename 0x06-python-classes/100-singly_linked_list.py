#!/usr/bin/python3
""" Node module """


class Node:
    """ Declares the Node class """

    def __init__(self, data, next_node=None) -> None:
        """
        Intializes the attributes of node class

        Args:
            data: value of node
            next_node:  address of next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets data of a linked list """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Gets next_node of a linked list """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Declares a class of SinglyLinkedList """

    def __init__(self) -> None:
        """ Intializes the private attribute """
        self.__head = None

    def __str__(self) -> str:
        """ returns string to be printed for SinglyLinkedList """
        output = list()
        future = self.__head

        while future is not None:
            output.append(str(future.data))
            future = future.next_node

        return "\n".join(output)

    def sorted_insert(self, value):
        """
        Sorts the node values

        Args:
            value: value of node
        """
        if self.__head is None:
            self.__head = Node(value)
            return

        if value < self.__head.data:
            self.__head = Node(value, self.__head)  # beginning of node
            return

        future, past = self.__head.next_node, self.__head
        while future is not None:
            if value < future.data:
                past.next_node = Node(value, future)    # middle of node
                return
            past = future
            future = future.next_node
        past.next_node = Node(value)    # end of node
