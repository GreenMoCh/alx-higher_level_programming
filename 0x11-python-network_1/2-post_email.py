#!/usr/bin/python3
"""POST an email #0"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        decode_response = response.read().decode('utf-8')
        print(decode_response)
