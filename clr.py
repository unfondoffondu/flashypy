
#I am rather proud of this piece, I think this, or something like it should be in the standard library for clearing the screen
#in the interpreter, as well as while running a script.
#it stashes the command clear in the variable clarity then echo's that into the shell.  I kept getting the output
#from clear, which is 0, so I hacked this together from something I saw on the internet.
#oh, this was before I discovered the void, aka /dev/null.

from os import system as sys

def clr():
	sys("clarity=$(clear);echo $clarity")

