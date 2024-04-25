#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods accepted by the server.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
