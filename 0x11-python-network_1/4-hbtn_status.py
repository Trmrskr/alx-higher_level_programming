#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    res = requests.get('https://alx-intranet.hbtn.io/status')
    txt = res.text
    print('Body response:')
    print('\t- type: {}'.format(type(txt)))
    print('\t- content: {}'.format(txt))
