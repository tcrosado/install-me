
class Message(object):

	def __init__(self):
		return


class Help(Message):
	def __init__(self):
		print("Valid Instructions:")
		print(" install [program name to search] - Tries to find a list of PPA's that most likely will have the program you are searching for ")

class Advice(Message):
	def __init__(self):
		print("GET REMINDED THAT I AM NOT RESPONSABLE BY ANY DAMAGE CAUSED BY PPA'S DOWNLOADED SOFTWARE")
		print("THIS PROGRAM AIMS ONLY TO MAKE IT EASY TO INSTALL SOFTWARE PRESENT IN PPAS")