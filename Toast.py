import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

#folder = r'C:\Users\PC 50\Desktop\Web Scrape\Icon' + '\\'


def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

i=1
soup = make_soup("URL##")
#print(soup)
for img in soup.findAll('img'):
	temp = img.get('src')
	if temp[:1]=="/":
		image = "URL##" + temp
	else:
		image = temp
	#print ""
	nametemp = img.get('alt')
	if nametemp:
		if len(nametemp)==0:
			filename=str(i)
			i=i+1
		else:
			filename = nametemp + str(i)
			i=i+1
		imagefile = open(filename + ".png", 'wb')
		imagefile.write(urllib.request.urlopen(image).read())
		imagefile.close()

		print ("done! [%s]" % (filename))