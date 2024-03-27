#!/bin/bash

# Sends a JSON POST request to a URL with the contents of a file in the body of the request

# Check if the filename is provided as an argument
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File $2 not found!"
    exit 1
fi

# Send the POST request with curl and check if the JSON is valid
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$2" -w "%{http_code}" "$1")

# Check if the response is 200 OK
if [ "$response" -eq 200 ]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
