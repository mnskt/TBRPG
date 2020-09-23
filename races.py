class Races():
	def __init__(self, race_name, hp, mp, attack, defence, racial_skill, race_description):
		self.race_name = race_name
		self.hp = hp
		self.mp = mp
		self.attack = attack
		self.defence = defence
		self.racial_skill = racial_skill
		self.race_description = race_description

orc = Races('Orc', 40, 0, 30, 30, 'Berserk', 'This is the orc race.')
elf = Races('Elf', 20, 30, 10, 10, 'Splash', 'This is the elf race')
dwarf = Races('Dwarf', 30, 15, 20, 20, 'Heal', 'This is the dwarf race')