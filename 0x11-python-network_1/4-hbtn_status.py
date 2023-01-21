#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res.text))
