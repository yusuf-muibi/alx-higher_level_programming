#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me_3 and captures the response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
