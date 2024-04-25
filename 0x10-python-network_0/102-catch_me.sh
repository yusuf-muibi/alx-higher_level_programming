#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and captures the response.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "You got me!"
