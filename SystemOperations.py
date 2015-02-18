import subprocess
import re




def getUbuntuCodeName():

	process = subprocess.Popen(["lsb_release", "-c"], stdout=subprocess.PIPE)
	output, err = process.communicate()
	codeName = output.decode("utf-8")
	codeName = re.sub("Codename:" or " ","",codeName)
		
	return codeName[1:-1]




