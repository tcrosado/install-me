#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.2 ALPHA
#


import sys
#import re

from SystemOperations import *
from PPAOperations import *
from PPALib import PPA
from Error import *
from Messages import * 


def install(searchTerm):
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
	return 



def options(args):
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
