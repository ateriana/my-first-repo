#!/usr/bin/python3
import sys
import requests

username = sys.argv[1]
password = sys.argv[2]

headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
}

response = requests.get('https://api.github.com/user', headers=headers)

print(response)