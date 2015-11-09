## Written by Sean Behan
## Copyright 2015

import os
#print (os.name)
import random

def get_chars(word):
	char_list = []
	for i in word:
		char_list.append(i)
	return char_list

def convert_underscore(word):
	underscores = ""
	for i in word:
		if i == " ":
			underscores += ("   ")
		else:
			underscores += (" _ ")
	for i in word:
		return underscores

def choose_topic():
	pick = input("Topics:\n\n1. Movies \n2. TV Shows \n3. Names\n\n(type /q to quit)\n\nEnter Topic: ")
	return pick

letters_to_choose = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wordlist = {
'movie' : ['spiderman', 'shrek', 'batman'],
'tv' : '',
'name' : ''
}

while True:
	topic_choice = choose_topic()
	print(topic_choice, type(topic_choice))
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
topic_char = get_chars(topic_pick)

print (convert_underscore(topic_pick))
guess_count = 10
while guess_count > 0:
	# re-init to false on every iteration
	correct_guess = False
	guess = input("\nGuesses Remaining: %i\n""Enter your Guess: " %(guess_count))
	in_letter_list = False

	for i in range(letters_to_choose):
		while in_letter_list == False:
			if i == letters_to_choose(i):
				in_letter_list = True
				item_to_remove = i

	for i in range(char_list):
		if guess == topic_char(i):
			correct_guess = True
			remove_item = i

	if correct_guess == False:
		guess_count -= 1
