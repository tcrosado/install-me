#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.1 ALPHA
#

import http.client
import re
from PPALib import PPA

def httpPageRequest(searchTerm):
	''' String -> String:
	httpPageRequest(searchTerm) returns the search result based 
	on the search term specified '''

	uniformSearchTerm = re.sub(' ', '+', searchTerm)
	pgReq = http.client.HTTPSConnection("launchpad.net")

	pgReq.request("GET","/ubuntu/+ppas?name_filter="+uniformSearchTerm)

	return str(pgReq.getresponse().read())



def parseURL(element):
	
	url = re.compile('<a href="(.*?)">', re.DOTALL).findall(element)

	return url[0]

def parseName(element):
	name = re.compile('">(.*?)</a>', re.DOTALL).findall(element)
	return name[0]

def parseInfo(element):
	desc = re.compile('<td>(.*?)</td>', re.DOTALL).findall(element)
	return desc[1:]

page = httpPageRequest("sublime text")
table = re.compile('<tr class="ppa_batch_row">(.*?)</tr>', re.DOTALL).findall(page)


ppaList = []
for element in table:
	url = parseURL(element)
	name = parseName(element)
	desc = parseInfo(element)

	print(desc)




#tes = PPA('name','http','desc',0,0)
#print(tes.getName())

