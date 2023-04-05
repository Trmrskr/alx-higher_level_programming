#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status and prints the body formated
"""

if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        output = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(output)))
        print('\t- content: {}'.format(output))
        print('\t- utf8 content: {}'.format(output.decode('utf-8')))
