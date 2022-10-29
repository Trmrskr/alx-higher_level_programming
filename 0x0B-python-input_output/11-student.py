#!/usr/bin/python3
"""This module contains the class ``Student``"""


class Student:
    """
        Student class defines the attribute of student

        Attribute:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
    """
    def __init__(self, first_name, last_name, age):
        """ Constructor function

            Argument:
                first_name: same as @Student.first_name attributes
                last_name: same as @Student.last_name attribute
                age: same as @Studen.age attribute
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ this function returns the __dict__ description of an instance """
        self_dict = self.__dict__

        if type(attrs) is list:
            attr_dict = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self_dict
                if attr in self.__dict__:
                    attr_dict.update({attr: self_dict[attr]})
            return attr_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the student instance """
        for key in json.keys():
            self.__dict__[key] = json[key]
