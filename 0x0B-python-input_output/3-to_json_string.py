#!/usr/bin/python3
""" to_json module """


import json


def to_json_string(my_obj):
    """
        function to generate a json from an object

        Args:
            my_obj: object
    """
    return json.dumps(my_obj)
