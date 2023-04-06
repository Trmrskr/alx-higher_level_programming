#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    length = len(commits) if len(commits) < 10 else 10
    for i in range(length):
        print(commits[i]['sha'], end=': ')
        print(commits[i]['commit']['author']['name'])
