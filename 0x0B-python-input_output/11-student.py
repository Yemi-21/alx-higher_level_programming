#!/usr/bin/python3
""" student module """


class Student:
    """ Student class """

    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """
            Constructor function

            Args:
                first_name:
                last_ame:
                age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Function generate a json from that class
        """
        json = {}

        if None is attrs:
            return self.__dict__

        for attr in attrs:
            if type(attr) is not str:
                continue
            if hasattr(self, attr):
                json[attr] = getattr(self, attr)

        return json

    def reload_from_json(self, json):
        """
            Function that force to load a json for an object
        """
        for key in json.keys():
            self.__dict__[key] = json[key]
