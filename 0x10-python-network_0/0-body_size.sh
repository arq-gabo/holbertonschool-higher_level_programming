#!/usr/bin/env bash
#Script of bash with show the size of the body of the response
size=$(curl -sI "$@" | awk '/Content-Length/{gsub("\\r", ""); print $2}')
echo $size
