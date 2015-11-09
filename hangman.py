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
list_movie = ['spider man','shrek','batman']
list_tv = []
list_name = []

while True:
	topic_choice = input("Topics:\n\n1. Movies \n2. TV Shows \n3. Names\n\n(type /quit to quit)\n\nEnter Topic: ")

	#print ('"'+topic_choice+'"')
	## Checks what number the user chose, uncomment this if we get errors with the list selection screen
	# if topic_choice == "/quit":
	# 	topic = 0
	# 	break
	# else:

	if topic_choice == "/quit":
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
#os.system('cls' if os.name == 'nt' else 'clear')

## Remember to get rid of this line for the end user
print ("\n",topic_pick,"\n")

print (convert_underscore(topic_pick))
user_guess_remaining = 10
for i in range(10):
	user_guess = input("\nGuesses Remaining: %i\n""Enter your Guess: " %(user_guess_remaining))
	user_guess_remaining -= 1
