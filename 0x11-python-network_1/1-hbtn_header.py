#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id variable."""
import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
