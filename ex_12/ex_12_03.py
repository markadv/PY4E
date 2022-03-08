from msilib.schema import Error
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter initial url: ')
count = input('Enter number of iterations: ')
count = int(count)
inicount = count
position = input('Enter link position: ')
position = int(position) - 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print (tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')