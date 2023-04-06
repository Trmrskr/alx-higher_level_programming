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
    search_key = 'id'
    try:
        res = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if search_key in res:
            print(res['id'])
        else:
            print(None)
