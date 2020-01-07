#!/usr/bin/env bash
#Script of bash with show the size of the body of the response
#curl -sI "$@" | awk '/Content-Length/{gsub("\\r", ""); print $2}'
curl -sI "$1" | grep "^Content-Length" | cut -d ' ' --fields=2
