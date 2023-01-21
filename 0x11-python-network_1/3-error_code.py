#!/usr/bin/python3

"""
Write a python script that takes in a URL, sends a request to the URL and 
displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as h:
        print('Error code: {}'.format(h.code))
