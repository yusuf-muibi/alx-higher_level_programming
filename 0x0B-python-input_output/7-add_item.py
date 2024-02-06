#!/usr/bin/python3
"""This function adds all arguments to a Python list and save them to a file"""
import sys

from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

try:
    existing_list = load_from_json_file("add_item.json")
    
except FileNotFoundError:
    existing_list = []

existing_list.extend(sys.argv[1:])

save_to_json_file(existing_list, "add_item.json")
