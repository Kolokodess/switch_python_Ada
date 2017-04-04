#A Simple fun game that allows a user make guess inputs from a number range of 1-50
#
#Oyom,Ada Nduka - 3/04/2017
#

import random

print "==========Welcome==========="
print "\nI Think of a number between 1-50 and All you have to do is make a simple guess"
print "\nI\'ll tell you if you are right or wrong, you have 5 chances"

# correct_number = random.randrange(50) + 1
# number_guess = int(raw_input("Take a guess from 1-50: "))
# tries = 0
# count = 0

def correct_guess(correct_number,tries): 
	#if number_guess == correct_number:
		print "Yes!, you guessed it right! The number was ", correct_number
		print "Number of tries: ", tries
		print "\n\n================Goodbye=================="
def number():
	#while number_guess != correct_number:
	correct_number = random.randrange(50) + 1
	number_guess = -1
	tries = 0
	count = 0
	#print correct_number
	while number_guess != correct_number:
		tries += 1
		count += 1
		if tries == 5:
			print "\n\n \Sorry You have exceeded the number of chances given to you"
			break
		number_guess = int(raw_input("Take a guess from 1-50: "))
		if number_guess > correct_number:
			print "========================="
			print "\n\nSorry that is a bit high, make another guess: \n"

		elif number_guess < correct_number:
			print "========================="
			print "\n\n Oops That\'s Lesser Than what i\'m thinking of, make another try: \n"

		else:
			correct_guess(correct_number,tries);
	# tries += 1
	# count += 1

number()
