#!/bin/bash
# This script sends a JSON POST request with file contents to a URL and displays the response body.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
