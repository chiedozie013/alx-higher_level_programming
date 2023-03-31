#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import urllib.request
import sys

# get the URL and email from the command line arguments
url = sys.argv[1]
email = sys.argv[2]

# encode the email as a byte string
email_bytes = email.encode('utf-8')

# send a POST request to the URL with the email as a parameter
with urllib.request.urlopen(url, data=email_bytes) as response:
    # decode the body of the response as utf-8
    body = response.read().decode('utf-8')
    print(body)
