#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods accepted by the server.
curl -s -X OPTIONS -i "$1" | grep -i Allow | awk '{print $2}'
