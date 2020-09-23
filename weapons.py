class Weapons():
	def __init__(self, name, atk_type, dmg):
		self.name = name
		self.atk_type = atk_type
		self.dmg = dmg

sword = Weapons('2 handed Great Sword', 'Slashing', 10)
dagger = Weapons('Magical dagger', 'Stabbing', 2)
mace = Weapons('Mace', 'Bludgeoning', 6)