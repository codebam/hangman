## Written by Sean Behan, 2014
## Copyright 2014

import os
#print (os.name)
import random
def convert_underscore(topic):
	underscores = ""
	for i in topic:
		if i == " ":
			underscores += ("   ")
		else:
			underscores += (" _ ")
	for i in topic:
		return underscores

def choose_topic(topic_choice):
	print("Topics:\n\n1. Movies \n2. TV Shows \n3. Names\n\n(type /quit to quit)\n\nEnter Topic: ")

## Lists of words to choose from
wordlist = {
'movie' : ['spiderman', 'shrek', 'batman'],
'tv' : '',
'name' : ''
}

while True:
	topic_choice = input("Topics:\n\n1. Movies \n2. TV Shows \n3. Names\n\n(type /quit to quit)\n\nEnter Topic: ")

	#print ('"'+topic_choice+'"')
	## Checks what number the user chose, uncomment this if we get errors with the list selection screen
	# if topic_choice == "/quit":
	# 	topic = 0
	# 	break
	# else:

	if topic_choice == "/quit" or "/q":
		quit()

	if topic_choice == "1":
		topic = list_movie
		break
	elif topic_choice == "2":
		topic = list_tv
		break
	elif topic_choice == "3":
		topic = list_name
		break
	else:
		print ("\nSorry, That's not a valid choice, please choose again:\n")

topic_pick = random.choice(topic)
## Enable this when you're done debugging
#os.system('cls' if os.name == 'nt' else 'clear')

## Remember to get rid of this line for the user
print ("\n",topic_pick,"\n")

print (convert_underscore(topic_pick))
guess_count = 10
while guess_count > 0:
	correct_guess = False
	# re init to false on every iteration
	guess = input("\nGuesses Remaining: %i\n""Enter your Guess: " %(guess_count))
	if correct_guess == False:
		guess_count -= 1
