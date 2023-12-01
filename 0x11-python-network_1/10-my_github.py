#!/usr/bin/python3
"""My GitHub!"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)

    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
