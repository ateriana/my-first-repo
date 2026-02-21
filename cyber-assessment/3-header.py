#!/usr/bin/python3
import urllib
import sys

#url = input("Enter url: ")
urllib.request.urlopen("https://httpbin.org/response-headers?X-Request-Id=hello_world")