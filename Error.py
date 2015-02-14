
''' Error class handles every error message used by the program '''

class Error(Exception):

	def __init__(self):
		print("Error:",end=" ")
		


class FewArgumentsError(Error):

	def __init__(self):
		super().__init__()
		print("Few Arguments")
		print("Run the program with 'help' as argument to get help")


class InvalidOptionError(Error):

	def __init__(self):
		super().__init__()
		print("Invalid Option")
