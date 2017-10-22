import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import os
import queue

#ignore ssl certification errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

headers={'User-agent' : "Mozilla/5.0"}

found={}

def crawldfs(url):

	if(url == None or ("https://en.wikipedia.org"+url) in found ):
		return

	if(url.find("/wiki/") != 0 or url.find("(") != -1 or url.find(":") != -1 ):
		return


	try:
		url="https://en.wikipedia.org"+url
		
		req=urllib.request.Request(url,None,headers)

		page=urllib.request.urlopen(req)

		cont=page.read()

	except:

		return

	found[url]=1;

	print(url)

	bsoup = BeautifulSoup(cont,"html.parser")

	anchor = bsoup('a')

	for link in anchor:

		crawldfs(link.get('href',None))


def crawlbfs(urlbegin):

	q=queue.Queue()
	
	q.put(urlbegin)

	while(not q.empty()):
		
		url=q.get()

		if(url == None or ("https://en.wikipedia.org"+url) in found ):
			continue

		if(url.find("/wiki/") != 0 or url.find("(") != -1 or url.find(":") != -1 ):
			continue


		try:
			url="https://en.wikipedia.org"+url
			
			req=urllib.request.Request(url,None,headers)

			page=urllib.request.urlopen(req)

			cont=page.read()

		except:

			continue

		found[url]=1;

		print(url)

		bsoup = BeautifulSoup(cont,"html.parser")

		anchor = bsoup('a')

		for link in anchor:

			q.put(link.get('href',None))


getfirst = input("ENTER STARTING URL: ")

x=input("Breadth or depth(0/1): ")

starter = getfirst[24:]

if(int(x)==1):
	crawldfs(starter)
else:
	crawlbfs(starter)
