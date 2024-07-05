#!/bin/bash
# Sends a requent to a URL passed as argument to it
curl -s "$1" | wc -c
