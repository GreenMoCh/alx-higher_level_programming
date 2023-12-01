#!/usr/bin/python3
"""What's my status? #0"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status of a given URL
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    status_info = {
            "type": str(type(content)),
            "content": content,
            "utf8_content": utf8_content
            }
    return status_info

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    status_info = fetch_status(url)

    print("Body response:")
    for key, value in status_info.items():
        print("    - {}: {}".format(key, value))
