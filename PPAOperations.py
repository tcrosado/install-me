import http.client
import re
from PPALib import PPA
from Error import InvalidOptionError

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
		print("PPA Author: " + ppa.getAuthor())
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
		
		condition = True
		while condition:
			
			print("Selet the PPA most likely to have the program you are looking for:(0 to exit)")
			
			id=int(input())

			if id == 0 : 
				exit()
			elif id > maxId:
				InvalidOptionError()
			else:
				condition = False


	except ValueError:		
		# Ends the program if other than a number is passed as input
		InvalidOptionError()
		exit()
		
	return listOfPPA[id-1]

def getPPAInfo(ppa):
	''' PPA -> [String,List of Strings]
	getPPAInfo(ppa) from a given ppa object, diplays the list of software from that PPA and confirms 
	with the user if the PPA has the software required by the user returning the name of that software
	and a list of lines to add to sources.list file'''

	url = ppa.getURL()
	page = httpRequestPage("launchpad.net",url)
	table = re.compile('<img src="/@@/package-source"(.*?)</td>', re.DOTALL).findall(page)
	softwareList = []

	# parsing info to add to sources.list
	preParse = re.compile('<pre id="sources-list-entries" class="wrap">(.*?)</pre>', re.DOTALL).findall(page)
	
	finalParse = re.sub("<(.*?)>", "", preParse[0])
	
	ppaSources = finalParse.split("\\n")


	
	while '' in ppaSources:
		# make sure it doesn't return empty strings
		ppaSources.remove('')
	
	print('################################################')	
	print("Software List avaliable in " + ppa.getName() + " :\n")
	for element in table:
		name = element[21:-16]
		if name not in softwareList:
			softwareList.append(name)
			print(name+"\n")

	print('################################################')


	condition = True
	while condition:
		print("Write down the software you want to install matching the list: (0 to exit)")
		
		softwareName = input()

		if softwareName not in softwareList:
			if softwareName == '0':
				exit()
			InvalidOptionError()
		else:
			condition = False

	# Need to return software name and deb lines

	return [softwareName,ppaSources]
	
	

