#!/bin/bash
# Displays all HTTP methods the server will accetps
curl -LIs "$1" | grep "Allow:" | cut -d' ' -f2-
