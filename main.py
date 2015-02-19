#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 1.0.0
#


import sys

from SystemOperations import *
from PPAOperations import *
from PPALib import PPA
from Error import *
from Messages import * 


def install(searchTerm):
	''' String -> {}
	install(searchTerm) proceeds with the main process of installing 
	a software based on the searchTerm given.
	Firstly shows a list of PPA's that might have the sofware the user
	is looking for, then confirms by presenting the list of sofware 
	avaliable on the selected PPA proceeding with the confirmation of 
	the software name with the user and then aplies all the bash 
	commands needed to install the selected software with user 
	confirmation
	'''
	ppa = selectPPA(searchTerm)
	[name,sources] = getPPAInfo(ppa)
	
	Message().advice()

	Message().addRepo(ppa.getName())
	Message().install(name)
	
	
	condition = True

	while condition:

		Message().proceed()
		
		op = input()

		if (op == 'Y'):
			condition = False
		elif (op == 'N'):
			exit()
		else:
			InvalidOptionError()

	
	#replacing YOUR_UBUNTU_VERSION_HERE with the actual version 

	for i in range(len(sources)):
		sources[i] = re.sub("YOUR_UBUNTU_VERSION_HERE",getUbuntuCodeName(),sources[i])
		addRepository(sources[i])

	aptUpdate()
	aptInstall(name)
	
	return 



def options(args):
	'''	String -> {}
	options(args) receives the arguments passed by the user when 
	launching the program via terminal
	'''
	try:
		if (args[1] == "install"):
		
			install(" ".join(args[2:]))
			
		elif (args[1] == "help"):
			Message().help()
		else:
			InvalidOptionError()

	except IndexError:
		FewArgumentsError()

	
options(sys.argv)
