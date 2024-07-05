#!/bin/bash
# Sends a GET request to a URL passed as argument and display the body of the respond
curl -LsH "X-School-User-Id: 98" "$1"
