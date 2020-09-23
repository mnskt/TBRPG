import cmd
import sys
import os
import time
import random
import classes

screen_width = 100

# Player Setup
class Player():
	def __init__(self):
		self.name = ''
		self.age = 0
		self.gender = ''
		self.race = ''
		self.klass = ''
		self.weapon = ''
thePlayer = Player()

def text_write(value):
	for character in value:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)

def game_setup():
	os.system('clear&cls')
	# Get Name
	obtain_name = "Hello, what's your name?\n"
	text_write(obtain_name)
	player_name = input(">>> ")
	thePlayer.name = player_name

	# Get Age
	obtain_age = "And what is your age?\n"
	text_write(obtain_age)
	player_age = input(">>> ")
	thePlayer.age = player_age

	# Get gender
	obtain_gender = "Are you male or female?\n"
	text_write(obtain_gender)
	player_gender = input(">>> ")
	acceptable_genders = ['male', 'female']

	while player_gender.lower() not in acceptable_genders:
		print("Unacceptable gender, try again")
		player_gender = input(">>> ")

	thePlayer.gender = player_gender.lower()
	print("Your name is " + thePlayer.name + ".")
	print("Your are " + thePlayer.age + " years old.")
	print("Your are " + thePlayer.gender + ".")

	# Get class
	obtain_class = "Which class are you?\nAvailable classes are: warrior, mage and cleric.\n"
	text_write(obtain_class)
	player_class = input(">>> ")

	while player_class.lower() not in ['warrior', 'mage', 'cleric']:
		print("Unavailable option, try again")
		player_class = input(">>> ")
		if player_class == ('warrior'):
			thePlayer.klass = classes.warrior_class
			print("You have successfully chosen the warrior class!")
		elif player_class == ('mage'):
			thePlayer.klass = classes.mage_class
			print("You have successfully chosen the mage class!")
		elif player_class == ('cleric'):
			thePlayer.klass = classes.cleric_class
			print("You have successfully chosen the cleric class!")
	else:
		if player_class == ('warrior'):
			thePlayer.klass = classes.warrior_class
			print("You have successfully chosen the warrior class!")
		elif player_class == ('mage'):
			thePlayer.klass = classes.mage_class
			print("You have successfully chosen the mage class!")
		elif player_class == ('cleric'):
			thePlayer.klass = classes.cleric_class
			print("You have successfully chosen the cleric class!")

	print(thePlayer.klass.description)

def title_screen():
	os.system("clear&cls")
	print("########################")
	print("#  -Welcome to TBRPG-  #")
	print("########################")
	print("###   - New Game -   ###")
	print("###     - Help -     ###")
	print("###     - Exit -     ###")
	print("########################")
	title_screen_nav()

def title_screen_nav():
	title_screen_option = input(">>> ")
	acceptable_choices = ['new game', 'help', 'exit']
	while title_screen_option.lower() not in acceptable_choices:
		print("Unavailable option, try again")
		title_screen_option = input(">>> ")
		if title_screen_option.lower() == ("new game"):
			game_setup()
		elif title_screen_option.lower() == ("help"):
			help_menu()
		elif title_screen_option.lower() == ("exit"):
			sys.exit()
	else:
		if title_screen_option.lower() == ("new game"):
			game_setup()
		elif title_screen_option.lower() == ("help"):
			help_menu()
		elif title_screen_option.lower() == ("exit"):
			sys.exit()

def help_menu():
	print("########################")
	print("#  -Welcome to TBRPG-  #")
	print("########################")
	print("Help description.")
	title_screen_nav()

title_screen()