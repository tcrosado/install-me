#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.2 ALPHA
#

import http.client
import re
import sys

from PPALib import PPA
from Error import *
from Messages import * 

def httpPageRequest(searchTerm):
	''' String -> String:
	httpPageRequest(searchTerm) returns the search result based 
	on the search term specified '''

	uniformSearchTerm = re.sub(' ', '+', searchTerm)
	pgReq = http.client.HTTPSConnection("launchpad.net")

	pgReq.request("GET","/ubuntu/+ppas?name_filter="+uniformSearchTerm)

	return str(pgReq.getresponse().read())

def ppaSearch(searchTerm):
	''' String -> List of PPA's
	ppaSearch(searchTerm) return a list of PPA Objects containg every PPA
	found during the search '''

	page = httpPageRequest(searchTerm)
	table = re.compile('<tr class="ppa_batch_row">(.*?)</tr>', re.DOTALL).findall(page)

	repList = []

	for element in table:
		repList.append(PPA(element))

	return repList

def ppaList(listOfPPA):
	''' List of PPA's 
	ppaList(listOfPPA) prints the localID, name, description, 
	number of sources and binaries of every PPA in the given list returning 
	the number of PPA's  of that list'''

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

def ppaSelect(searchTerm):
	listOfPPA = ppaSearch(searchTerm)
	maxId=ppaList(listOfPPA)
	
	try:
		print("Selet the PPA most likely to have the program you are looking for:(0 to exit)")
		id =int(input())
		while id>maxId:
			InvalidOptionError()
			print("Input a valid PPA ID:")
			id=int(input())
		if (id == 0) :
			exit()
	except ValueError:		
		# Ends the program if other than a number is passed as input
		InvalidOptionError()
		#TESTING 
		return -1

	return listOfPPA[id]

def install(searchTerm):
	ppa = ppaSelect(searchTerm)
		


	return 



def Options(args):
	try:
		if (args[1] == "install"):
		
			install(" ".join(args[2:]))
		
		elif (args[1] == "help"):
			Help()
		else:
			InvalidOptionError()

	except IndexError:
		FewArgumentsError()

	
Options(sys.argv)
