#	Author : Tiago Rosado (speedofthesea)
#
#	Version : 0.0.2 ALPHA
#
import re

'''
	PPA class stores a basic information of a PPA. 
'''
class PPA(object):

	_name = ''
	_author = ''
	_url  = ''
	_description = '' 
	_sources = 0
	_binaries = 0

	def __init__(self,element):
		parser = Parser(element)

		self._name = parser.parseName()
		self._author = parser.parseAuthor()
		self._url = parser.parseURL()
		self._description, self._sources, self._binaries = parser.parseInfo()
		
		
	def getName(self):
		return self._name

	def getAuthor(self):
		return self._author

	def getURL(self):
		return self._url

	def getDescription(self):
		return self._description

	def getSources(self):
		return self._sources

	def getBinaries(self):
		return self._binaries


''' 
	Parser class handles pre-parsed elements comming from the search result.
This class parses each information element found into diferent types compatible 
with the PPA class. 
'''
class Parser(object):
		
		def __init__(self,element):
			self._element = element

		
		def parseName(self):
			name = re.compile('">(.*?)</a>', re.DOTALL).findall(self._element)
			return name[0]

		def parseURL(self):
			url = re.compile('<a href="(.*?)">', re.DOTALL).findall(self._element)

			return url[0]

		def parseAuthor(self):
			author = re.compile('/~(.*?)/', re.DOTALL).findall(self.parseURL())
			return author[0]

		def parseInfo(self):
			desc = re.compile('<td>(.*?)</td>', re.DOTALL).findall(self._element)
			return desc[1:] 

		