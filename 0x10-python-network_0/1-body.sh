#!/bin/bash
# Sends a GET request to a URL passed as argument and follows its redirections
curl -L -X GET "$1"
