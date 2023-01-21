#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a paramter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib import parse
    from urllib import request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')

    with request.urlopen(argv[1]) as res:
        body = res.read().decode('utf-8')
        print('Your email is: {}'.format(body.email))
