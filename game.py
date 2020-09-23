import cmd
import sys
import os
import time
import random
import classes
import races
import weapons

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
	obtain_age = "\nAnd what is your age?\n"
	text_write(obtain_age)
	player_age = input(">>> ")
	thePlayer.age = player_age

	# Get gender
	obtain_gender = "\nAre you male or female?\n"
	text_write(obtain_gender)
	player_gender = input(">>> ")
	acceptable_genders = ['male', 'female']

	while player_gender.lower() not in acceptable_genders:
		print("Unacceptable gender, try again")
		player_gender = input(">>> ")

	thePlayer.gender = player_gender.lower()

	# Get class
	obtain_class = "\nWhich class are you?\nAvailable classes are: warrior, mage and cleric.\n"
	text_write(obtain_class)
	player_class = input(">>> ")

	while player_class.lower() not in ['warrior', 'mage', 'cleric']:
		print("Unavailable option, try again")
		player_class = input(">>> ")
		if player_class == ('warrior'):
			thePlayer.klass = classes.warrior_class
		elif player_class == ('mage'):
			thePlayer.klass = classes.mage_class
		elif player_class == ('cleric'):
			thePlayer.klass = classes.cleric_class
	else:
		if player_class == ('warrior'):
			thePlayer.klass = classes.warrior_class
		elif player_class == ('mage'):
			thePlayer.klass = classes.mage_class
		elif player_class == ('cleric'):
			thePlayer.klass = classes.cleric_class

	# Get race
	obtain_race = '\nAnd what race would you be?\nAvailable races are: orc, elf and dwarf.\n'
	text_write(obtain_race)
	available_races = ['orc', 'elf', 'dwarf']
	player_race = input(">>> ")

	while player_race.lower() not in available_races:
		print("Unavailable option, try again\n")
		player_race = input(">>> ")
		if player_race == ('orc'):
			thePlayer.race = races.orc
		if player_race == ('elf'):
			thePlayer.race = races.elf
		if player_race == ('dwarf'):
			thePlayer.race = races.dwarf
	else:
		if player_race == ('orc'):
			thePlayer.race = races.orc
		if player_race == ('elf'):
			thePlayer.race = races.elf
		if player_race == ('dwarf'):
			thePlayer.race = races.dwarf
	
	# Get starting weapon
	obtain_weapon = '\nWhich weapon would you like to start with?\nAvailable weapons are: sword, dagger, mace.\n'
	text_write(obtain_weapon)
	avaiable_weapons = ['sword', 'dagger', 'mace']
	player_start_weapon = input(">>> ")

	while player_start_weapon.lower() not in avaiable_weapons:
		print("Unavailable option, try again\n")
		player_start_weapon = input(">>> ")
		if player_start_weapon == ('sword'):
			thePlayer.weapon = weapons.sword
		elif player_start_weapon == ('dagger'):
			thePlayer.weapon = weapons.dagger
		elif player_start_weapon == ('mace'):
			thePlayer.weapon = weapons.mace
	else:
		if player_start_weapon == ('sword'):
			thePlayer.weapon = weapons.sword
		elif player_start_weapon == ('dagger'):
			thePlayer.weapon = weapons.dagger
		elif player_start_weapon == ('mace'):
			thePlayer.weapon = weapons.mace

	# Created character display
	os.system("clear&cls")
	print("###############################")
	print("### Your created character  ###")
	print("###############################")
	print("Name: " + thePlayer.name)
	print("Gender: " + thePlayer.gender)
	print("Age: " + thePlayer.age)
	print("Race: " + thePlayer.race.race_name)
	print("Class: " + thePlayer.klass.name)
	print(f"HP: {thePlayer.klass.baseHP + thePlayer.race.hp}")
	print(f"MP: {thePlayer.klass.baseMP+thePlayer.race.mp}")
	print(f"Attack: {thePlayer.klass.baseAtk + thePlayer.race.attack}")
	print(f"Defence: {thePlayer.klass.baseDef + thePlayer.race.defence}")
	print("Racial skill: " + thePlayer.race.racial_skill + "\n")
	print("Main weapon: "+ thePlayer.weapon.name)
	print("Weapon's damage type: " + thePlayer.weapon.atk_type)
	print(f"Weapon's damage: {thePlayer.weapon.dmg}")
	print("###############################")


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