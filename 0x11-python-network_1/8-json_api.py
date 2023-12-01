#!/usr/bin/python3
"""Search API"""

import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_data = response.json()

        if json_data and 'id' in json_data and 'name' in json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")

    except:
        print("Not a valid JSON")
