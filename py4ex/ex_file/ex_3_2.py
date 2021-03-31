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

nu ='http://py4e-data.dr-chuck.net/known_by_Eilish.html'


# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
count = input('Enter count: ')
position = input('Enter position: ')

c = int(count)
p = int(position)
# Retrieve all of the anchor tags
ltags = list()
otags = list()
for i in range(c):
    nhtml = urllib.request.urlopen(nu,context=ctx).read()
    soup = BeautifulSoup(nhtml,'html.parser')
    tags = soup('a')
    for tag in tags:
        ltags.append(tag.get('href',None))
    otags.append(ltags[p-1])
    nu = otags[i]
    ltags.clear()

for t in otags:
    print(t)
