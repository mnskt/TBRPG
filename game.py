import cmd
import sys
import os
import time
import random

screen_width = 100

# Player Setup
class Player():
	def __init__(self):
		self.name = ''
		self.age = 0
		self.gender = ''
		self.race = ''
		self.klass = ''

thePlayer = Player()

def game_setup():
	os.system('clear&cls')
	# Get Name
	obtain_name = "Hello, what's your name?\n"
	for character in obtain_name:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	player_name = input(">>> ")
	thePlayer.name = player_name
	# Get Age
	obtain_age = "And what is your age?\n"
	for character in obtain_age:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	player_age = input(">>> ")
	thePlayer.age = player_age
	# Get gender
	obtain_gender = "Are you male or female?\n"
	for character in obtain_gender:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	player_gender = input(">>> ")
	while player_gender.lower() not in ['male', 'female']:
		if player_gender.lower() == 'Male':
			thePlayer.gender = player_gender
		elif player_gender.lower() == "Female":
			thePlayer.gender = player_gender
		else:
			print("Please select either male or female genders.")

	print("Your name is " + thePlayer.name + ".")
	print("Your are " + thePlayer.age + " years old.")
	print("Your are " + thePlayer.gender + ".")

game_setup()