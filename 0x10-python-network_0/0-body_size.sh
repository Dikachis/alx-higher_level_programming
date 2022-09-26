#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

# The script should be found when search: 
# https://stackoverflow.com/questions/4497759/how-to-get-remote-file-size-from-a-shell-script
# but, we want to pass the URL as an argument in the command line, therefore we replace URL with $1;

curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
