# Peer Review for the Application Below
# Author: Patrick Grieve
# Creation Date: 9/19/2022
# Below is a simple program with a few issues some are syntax errors and some are logic errors.
#Peer Review:
# 1. A few of the things I found were that on line 13 there is an indentation error with "while cave != '1' and cave != '2'.
# 2. Another mistake would be on The variable caves is not defined, the variable name "cave" is used for this purpose, there is just a spelling mistake.
# 3. Another error was on line 47, where we are calling the function choosecave(), but we have defined the function chooseCave().
# 4. There is a spelling mistake in playing in the final line.
# 5. There is a mistake on the code "return caves, it should say return cave.
# 6. Some of the print() functions need to be corrected in the right syntax. 

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")




