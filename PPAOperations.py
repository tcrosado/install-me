import http.client
import re
from PPALib import PPA

def httpRequestPage(site,url):
	''' String,String -> String
	httpRequestPage(site,url) handels the actual HTTP request for the page specified in "url" of 
	the site passed as argument and returns a sring with the actual page'''

	conn = http.client.HTTPSConnection(site)

	conn.request("GET",url)

	return str(conn.getresponse().read())

def requestPPAList(searchTerm):
	''' String -> String:
	requestPPAList(searchTerm) returns the search result based 
	on the search term specified '''

	uniformSearchTerm = re.sub(' ', '+', searchTerm)

	return httpRequestPage("launchpad.net","/ubuntu/+ppas?name_filter="+uniformSearchTerm)

def searchPPA(searchTerm):
	''' String -> List of PPA's
	searchPPA(searchTerm) return a list of PPA Objects containg every PPA
	found during the search '''

	page = requestPPAList(searchTerm)
	table = re.compile('<tr class="ppa_batch_row">(.*?)</tr>', re.DOTALL).findall(page)

	repList = []

	for element in table:
		repList.append(PPA(element))

	return repList

def listPPAS(listOfPPA):
	''' List of PPA objects -> Int
	listPPAS(listOfPPA) prints the localID, name, description, 
	number of sources and binaries of every PPA in the given list 
	returning the number of PPA's  of that list'''

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

def selectPPA(searchTerm):
	''' String -> PPA
	selectPPA(searchTerm) for a given searchTerm gets a list of PPA's 
	and asks the user to select one PPA from that list returning the
	PPA object selected by the user'''

	listOfPPA = searchPPA(searchTerm)
	maxId=listPPAS(listOfPPA)
	
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
		exit()
		
	return listOfPPA[id-1]

def getPPAInfo(ppa):
	url = ppa.getURL()
	page = httpRequestPage("launchpad.net",url)
	table = re.compile('<img src="/@@/package-source"(.*?)</td>', re.DOTALL).findall(page)
	print("Software List avaliable in " + ppa.getName() + " :")
	for element in table:
		print(element[21:-16])
	
