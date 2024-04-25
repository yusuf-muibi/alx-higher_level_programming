#!/bin/bash
# This script takes a URL as an argument, sends a request to the URL using curl, and displays the size of the response body in bytes.
curl -s "$1" | wc -c
