#!/bin/bash
# Sends a POST request to the URL passed as argument and display the body of the response
curl -Lsd "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD" "$1"
