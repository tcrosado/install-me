
class Message(object):

	def __init__(self):
		return

	def help(self):
		print("Valid Instructions:")
		print(" install [program name to search] - Tries to find a list of PPA's that most likely will have the program you are searching for ")

	def advice(self):
		print("\nGET REMINDED THAT I AM NOT RESPONSABLE BY ANY DAMAGE CAUSED BY PPA'S DOWNLOADED SOFTWARE")
		print("THIS PROGRAM AIMS ONLY TO MAKE IT EASY TO INSTALL SOFTWARE PRESENT IN PPAS")

	def proceed(self):
		print("Do you want to proceed?(Y to continue/N to exit)")

	def addRepo(self,name):
		print("You are about to add "+name+" to your local PPA repository.")

	def install(self,name):
		print("You are about to install " + name + " on your Ubuntu machine.\n")