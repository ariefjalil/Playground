#!/usr/bin/env Python


""" Guesser.py by Arief Jalil, 13.10.2017
This program has user guess a number between
1 and 100.
"""
import random
rand = random.randint(1,100)

while True:

	print "Please enter a number:"
	userGuess = int(raw_input())

	if userGuess == rand:
		print "You got it!"
		break

	if userGuess > rand:
		print "CHOOSE LOWER NUMBER"
	elif userGuess < rand:
		print "CHOOSE HIGHER"

	else:
		print "Nope, that's not it!"