#!/bin/bash
# Sends a POST request to a URL with specific parameters and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
