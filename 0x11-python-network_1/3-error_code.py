#!/usr/bin/python3
"""Error code #0"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            decode_response = response.read().decode('utf-8')
            print(decode_response)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
