#!/usr/bin/python3
"""This defines a string to JSON function"""
import json

def to_json_string(my_obj):
    """Returns: str: The JSON representation of the object."""
    return json.dumps(my_obj)
