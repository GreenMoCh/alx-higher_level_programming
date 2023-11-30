#!/bin/bash
# Check if URL is provided as an argument
curl -s "$1" | wc -c
