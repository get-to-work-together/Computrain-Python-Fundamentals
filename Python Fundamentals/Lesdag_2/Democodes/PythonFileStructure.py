#!/usr/bin/python3
import os
import sys

# Global variables

g_exampleVariable = "Global Example Variable" # Only, if this is necessary

# From here till the main function, functions have to be programmed. 
# An example function: showHelloWorld
def showHelloWorld(helloWorld):
	print()
	print(helloWorld)
	print()
	print(g_exampleVariable)
	print()
        
# The last function is always the main function, in which only other functions are called.
def main(argv):

	helloToUser = "Hello World!"
	
	showHelloWorld(helloToUser) # Example of a function.
                               
if __name__ == "__main__":
	main(sys.argv)
	
