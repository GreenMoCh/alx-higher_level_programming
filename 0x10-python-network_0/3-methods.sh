#!/bin/bash
# Script that takes in aURL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
