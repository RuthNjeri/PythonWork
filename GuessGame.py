#!/usr/bin/env python3
#Ruth Waiganjo Kamilimu Python Assignment

import random



rand = random.randint(0,100) #range of random integers between 0 and 100
print("---------------------------------------\n"+"\tGUESS THE NUMBER APP\n"+"---------------------------------------\n")

while rand: #the loop runs as long as the random number is available

	number = int(input('Guess a number between 0 and 100: ')) #convert input string to integer

	if number<rand:
		print("Sorry but",number ,"is LOWER than the number")

	if number>rand:
		print("Sorry but",number, "is HIGHER than the number")	

	if number == rand:
		print("YES! You've got it. The number was",number)
		break #The loop breaks when the game is won		


	
