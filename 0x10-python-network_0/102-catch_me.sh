#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and captures the response.
curl -sL -X PUT -d "user_id=98" http://0.0.0.0:5000/catch_me_3
