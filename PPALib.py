#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.1 ALPHA
#

class PPA(object):
	_name = ''
	_url  = ''
	_description = '' 
	_sources = 0
	_binaries = 0

	def __init__(self,name,url,description,sources,binaries):
		self._name = name
		self._url = url
		self._description = description
		self._sources = sources 
		self._binaries = binaries

	def getName(self):
		return self._name

	def getURL(self):
		return self._url

	def getDescription(self):
		return self._description

	def getSources(self):
		return self._sources

	def getBinaries(self):
		return self._binaries


