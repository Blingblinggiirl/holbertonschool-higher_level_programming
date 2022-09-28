#!/usr/bin/python3
"""     task 5      """


import json


def save_to_json_file(my_obj, filename):
    """ Save object to a file """
    with open(filename, 'w+') as file_open:
        file_open.write(json.dumps(my_obj))
