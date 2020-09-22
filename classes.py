class Classes:
	def __init__(self, name, baseHP, baseMP, baseAtk, baseDef, description):
		self.name = name
		self.baseHP = baseHP
		self.baseMP = baseMP
		self.baseAtk = baseAtk
		self.baseDef = baseDef
		self.description = description

warrior_class = Classes('Warrior', 120, 0, 30, 30, 'This is a fighter class.')
mage_class = Classes('Mage', 50, 140, 10, 10, 'This is a mage class.')
cleric_class = Classes('Cleric', 70, 70, 20, 20, 'This is a cleric class.')