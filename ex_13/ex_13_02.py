import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print ("Retrieving " + url)

jsontemp = urllib.request.urlopen(url, context=ctx).read() #copied from ex_12_03
print ("Retrieved: " + str(len(jsontemp)) + " characters") #characters based on len of jsontemp

data = json.loads(jsontemp) #as in tutorial, convert jsontemp to json

numcomments = len(data['comments']) #find the number of comments in the file
print ('Count:', numcomments)

accumulator = 0
for i in range(numcomments):
    accumulator += data['comments'][i]['count']

print ('Sum:', accumulator)