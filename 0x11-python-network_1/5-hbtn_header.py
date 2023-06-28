#!/usr/bin/python3
"""
 A Python script that takes in a URL, sends a request
 to the URL and displays the value of the X-Request-Id
 variable found in the header of the response.
 You must use "requests"
"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get("X-Request-Id"))
