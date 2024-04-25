#!/bin/bash
# This script sends a POST request to the URL with specified data and displays the response body.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
