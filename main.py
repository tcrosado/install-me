#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.1 ALPHA
#

import http.client
import re
import sys

from PPALib import PPA

def httpPageRequest(searchTerm):
	''' String -> String:
	httpPageRequest(searchTerm) returns the search result based 
	on the search term specified '''

	uniformSearchTerm = re.sub(' ', '+', searchTerm)
	pgReq = http.client.HTTPSConnection("launchpad.net")

	pgReq.request("GET","/ubuntu/+ppas?name_filter="+uniformSearchTerm)

	return str(pgReq.getresponse().read())

def ppaSearch(searchTerm):
	page = httpPageRequest(searchTerm)
	table = re.compile('<tr class="ppa_batch_row">(.*?)</tr>', re.DOTALL).findall(page)

	repList = []

	for element in table:
		repList.append(PPA(element))

	return repList

def ppaList(listOfPPA):
	print("-------------------------------------")
	id = 0
	for ppa in listOfPPA:
		id+=1
		print(str(id)+" - " + ppa.getName())
		print("Desc: " + ppa.getDescription())
		print("Sources: " + str(ppa.getSources()))
		print("Binaries: " + str(ppa.getBinaries()))
		print("-------------------------------------")
	
	return id

def Options(args):
	if (args[1] == "install"):
		maxId = ppaList(ppaSearch(args[2]))
		
		print("Chose the most likely ppa that has the software you need:")
		userOP = input()

		while int(userOP) not in range(maxId):

			print("Error : Invalid Option")
			userOP = input()
		
		print("You entered "+ userOP)
	else:
		print("Error : Invalid Option")

	
Options(sys.argv)
