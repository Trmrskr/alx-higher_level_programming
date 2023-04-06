#!/usr/bin/python3
"""
Takes your Github credentials and uses the GitHub API
to display your ID.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
