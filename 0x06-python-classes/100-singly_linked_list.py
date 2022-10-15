#!/usr/bin/python3
"""This file defines the Node class and the SinglyLinkedList
    class of a singly linked list"""


class Node:
    """Defines a node of a singly linked list (sll)

    Attributes:
        data: holdes data of the list
        next_node: the pointer to the next node of the list
    """

    def __init__(self, data, next_node=None):
        """The constructor method of the sll"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """The getter function of the data private instance variable"""
        return self.__data

    @data.setter
    def data(self, value):
        """the setter function of the data private instant variable"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """The getter function of the next node instance variable"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """The setter function of the next node instance variable"""
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            return TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """The class definition of the singly linked list which defines the
    node object

    Attributes:
        head: a private instance variable
    """
    def __init__(self):
        """The constructor method of singly linked list class"""
        self.__head = None

    def __str__(self):
        """The string implementation of the singly linked list class to define
            to define its behaviour when an instance is printed
        """
        sll_data = ""
        cur_node = self.__head

        while (cur_node is not None):
            sll_data += str(cur_node.data) + "\n"
            cur_node = cur_node.next_node

        return sll_data[:-1]

    def sorted_insert(self, value):
        """Sort and insert element into the singly linked list

        Arg:
            value: the element to be inserted to the SLL
        """
        cur_node = self.__head

        if type(value) is not int:
            raise TypeError("data must be an integer")

        if cur_node is None:
            self.__head = Node(value, self.__head)
            return
        if cur_node.data > value:
            self.__head = Node(value, cur_node)
            return
        while (cur_node.next_node is not None
                and cur_node.next_node.data < value):
            cur_node = cur_node.next_node
        cur_node.next_node = Node(value, cur_node.next_node)
