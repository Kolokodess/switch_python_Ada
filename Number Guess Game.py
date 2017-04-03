#A Simple fun game that allows a user make guess inputs from a number range of 1-50
#
#Oyom,Ada Nduka - 3/04/2017
#

import random

print "==========Welcome==========="
print "\nI Think of a number between 1-50 and All you have to do is make a simple guess"
print "I\'ll tell you if you are right or wrong, you have 5 chances"

correct_number = random.randrange(50) + 1
number_guess = int(raw_input("Take a guess from 1-50: "))
tries = 1
count = 0

while number_guess != correct_number:
	if tries ==(3)+1:
		print "\n\n \Sorry You have exceeded the number of chances given to you"
		break
	# print "========================="
	# print "\n\nSorry, make another guess: \n"

	if number_guess > correct_number:
		print "========================="
		print "\n\nSorry that is a bit high, make another guess: \n"

	elif number_guess < correct_number:
		print "========================="
		print "\n\n Oops That\'s Lesser Than what i\'m thinking of, make another try: \n"

	number_guess = int(raw_input("Take a guess from 1-50: "))
	tries =+1
	count =+1


if number_guess == correct_number:
	print "Yes!, finally you guessed it right! The number was ", correct_number
	print "Number of tries: ", tries

