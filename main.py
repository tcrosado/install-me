#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.2 ALPHA
#


import sys

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
