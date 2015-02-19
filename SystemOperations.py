import subprocess
import re
import os



def getUbuntuCodeName():
	''' {} -> String
	getUbuntuCodeName() returns the Ubuntu version code name based on
	"lsb_release" bash command ''' 
	process = subprocess.Popen(["lsb_release", "-c"], stdout=subprocess.PIPE)
	output, err = process.communicate()
	codeName = output.decode("utf-8")
	codeName = re.sub("Codename:" or " ","",codeName)
		
	return codeName[1:-1]


def addRepository(source):
	''' String -> {}
	addRepository(source) gets the source line as argument and 
	requiering root permissions adds the repository given to the local
	list of repositories'''

	print("Adding apt repository")
	process = subprocess.Popen(['sudo','add-apt-repository',source],stdout=subprocess.PIPE)
	output, err = process.communicate()
	test = output.decode("utf-8")
	
	return 

def aptUpdate():
	''' {} -> {}
	aptUpdate() runs the "apt-get update" bash command, requiering 
	root permissions to run it '''

	print("Updating apt (might take awhille)")

	process = subprocess.Popen(['sudo','apt-get','update'],stdout=subprocess.PIPE)
	output, err = process.communicate()
	
	return	

def aptInstall(softwareName):
	''' String -> {}
	aptInstall() runs the "apt-get install" bash command with the 
	softwareName passed as argument
	This functions need root permissions '''

	print("Installing "+softwareName) 

	os.system('sudo apt-get install '+softwareName)

	print("Installation Done")
	return 


	


