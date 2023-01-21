#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    res = requests.get('https://alx-intranet.hbtn.io/status')
    txt = res.text
    print('Body response:')
    print('\t- type: {}'.format(type(txt)))
    print('\t- content: {}'.format(txt))
