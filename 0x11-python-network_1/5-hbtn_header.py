#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request_Id in the response header
"""

if __name__ == '__main__':
    """
    An alternative solution is using the following line:
    `print(res.headers.get('X-Request-Id')`
    """
    import requests
    from sys import argv

    res = requests.get(argv[1])
    print(res.headers['X-Request-Id'])
