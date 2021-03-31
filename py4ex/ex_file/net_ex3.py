# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://py4e-data.dr-chuck.net/known_by_Fikret.html'


# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
count = input('Enter count: ')
position = input('Enter position: ')

c = int(count)
p = int(position)
# Retrieve all of the anchor tags
ltags = list()
otags = list()

def open_url(nurl):
    nhtml = urllib.request.urlopen(nurl,context=ctx).read()
    soup = BeautifulSoup(nhtml,'html.parser')
    tags = soup('a')
    for tag in tags:
        ltags.append(tag.get('href',None))
    # otags.append(ltags[p])

    return ltags

open_url(url)
nu = ltags[p]

for i in range(c):
    print(nu)
    open_url(nu)
    print(ltags[p])
    otags.append(ltags[p])
    c = c - 1
    nu = otags[i]
print(otags)
