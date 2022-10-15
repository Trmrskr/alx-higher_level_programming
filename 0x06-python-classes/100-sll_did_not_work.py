#!/usr/bin/python3
"""This file defines the Node class and the SinglyLinkedList class of a singly linked list"""


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
    """The class definition of the singly linked list which defines the node object

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
        cur_node = self.__head
        new_node = Node(value, cur_node)
        prev_node = None

        if type(value) is not int:
            raise TypeError("data must be an integer")

        while (cur_node is not None):
            if cur_node.data >= value:
                if prev_node is None:
                    prev_node = new_node
                    self.__head = prev_node
                    return
                else:
                    prev_node.next_node = new_node
                    return
            prev_node = cur_node
            cur_node = cur_node.next_node
        self.__head = new_node
