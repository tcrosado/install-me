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
	

	return 



def options(args):
	try:
		if (args[1] == "install"):
		
			install(" ".join(args[2:]))
		
		elif (args[1] == "help"):
			Help()
		else:
			InvalidOptionError()

	except IndexError:
		FewArgumentsError()

	
options(sys.argv)
