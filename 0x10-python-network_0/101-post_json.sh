#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file and displays the body of the response
if [ ! -f "$2" ]; then
    echo "File not found!"
    exit 1
fi
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
