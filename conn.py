#!/usr/bin/env python3
import requests as req
import os

def openConnection(url):
    resp = req.request(method='GET', url=url)
    if resp.status_code == 200:
        return resp
    else:
        print('Error accessing ' + url)

def writeFile(name, obj):
    if os.path.isfile(name):
        print( name + ' already exists. Please try another file name')
        return False
    else:
        try:
            with open(name, 'wb') as f:
                f.write(obj)
            return True
        except IOError:
            print( name + ' cannot be written to')
            return False

def main():
    url = input('URL: ')
    name = input('Filename: ')
    resp = openConnection(url)
    writeFile(name,resp.content)
    resp.close()

if __name__ == '__main__':
    main()




