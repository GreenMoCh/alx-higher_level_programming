#!/usr/bin/python3
"""Response header value #0"""

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')

    print(x_request_id)
