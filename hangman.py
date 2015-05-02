## Written by Sean Behan, 2014
## Copyright 2014

import os
#print (os.name)
import random
def ConvertToUnderscore(myL):
	cypherd = ""
	for i in myL:
		if i == " ":
			cypherd += ("   ")
		else:
			cypherd += (" _ ")
	for i in myL:

		return cypherd

## Lists of words to choose from
myMovies = ['spider man','shrek','batman']
myTV = []
myNames = []

while True:
	myListChoice = int(input("Topics:\n\n1. Movies \n2. TV Shows \n3. Names\n\nEnter Topic: "))

	#print ('"'+myListChoice+'"')
	## Checks what number the user chose, uncomment this if we get errors with the list selection screen
	if myListChoice == 1:
		myList = myMovies
		break
	elif myListChoice == 2:
		myList = myTV
		break
	elif myListChoice == 3:
		myList = myNames
		break
	else:
		print ("\nSorry, That's not a valid choice, please choose again:\n")

myChoice = random.choice(myList)
os.system('cls' if os.name == 'nt' else 'clear')

## Remember to get rid of this line for the end user
print ("\n",myChoice,"\n")

print (ConvertToUnderscore(myChoice))
userGuessesRemaining = 10
for i in range(10):
	userGuess = input("\nGuesses Remaining: %i\n""Enter your Guess: " %(userGuessesRemaining))
	userGuessesRemaining -= 1
