#!/usr/bin/python3
import sys
import requests

username = sys.argv[1]
password = sys.argv[2]

data = requests.get(f"https://api.github.com/user/{username}")
print(data)