#!/usr/bin/python3
""" returns the JSON rep of an object (string) """


import json


def to_json_string(my_obj):
    """ JSON to string """
    return json.dumps(my_obj)
