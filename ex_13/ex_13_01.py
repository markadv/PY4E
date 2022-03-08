import urllib.request, urllib.parse, urllib.error
import urllib
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print ("Retrieving " + url)

xml = urllib.request.urlopen(url, context=ctx).read() #copied from ex_12_03
print ("Retrieved: " + str(len(xml)) + " characters") #characters based on len of xml

tree = ET.fromstring(xml) #as in tutorial, convert xml with xml.etree.ElementTree as ET

counts = tree.findall('.//count') #XPath selector string, as in instructions
print("Count:", len(counts))

sum = 0
for count in counts:
    sum = sum + int(count.text)

print ('Sum:',sum)