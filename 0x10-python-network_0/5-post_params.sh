#!/bin/bash
# Script that sends a POST request to the URL, and displays the body of the response with 200 status code
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST ${1}
