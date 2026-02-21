#!/usr/bin/python3
import sys
import requests

username = sys.argv[1]
password = sys.argv[2]

headers = {
    'Authorization': f'Bearer {password}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
}
try:
    user_info = requests.get('https://api.github.com/user', headers=headers).json()

    user_id = user_info["id"]

    print(user_id)
except:
    print(None)