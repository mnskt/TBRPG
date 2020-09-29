def draw_board(board):
	line = '------------------------------'

	for row in range(9, -1, -1):
		print(f'\n{line}\n', end='')
		for pos in range(row*10, row*10+10):
			print(f' {board[pos]} |', end='')

theBoard = [" " for i in range(0, 100)]

class Player():
	def __init__(self, name, player, location):
		self.name = name
		self.player = player
		self.location = location

char = Player("P", " ", 0)

def game_action():
	game_action_dict = {
		"up": (0, 10),
		"down": (0, -10),
		"left": (-1, 0),
		"right": (1, 0)
	}

	while True:
		game_action = input("Type")
		if game_action in game_action_dict:
			try:
				game_action_dict[game_action]()
			except TypeError:
				makeMove(game_action_dict[game_action])
		else:
			print("Unknown command...")

def makeMove(move):
	pos = char.location
	valid = False
	if move[0] == 0:  # if move is a vertical move
		if 0 <= pos + move[1] <= 99:
			valid = True

	elif move[1] == 0:
		row = (pos // 10) * 10
		if row <= pos + move[0] <= row + 9:  # if position after move is between x0 and x9 e.g 40-49
			valid = True

	elif move[0] == move[1]:  # if move is zero movement
		valid = True

	if not valid:
		print("Out of bounds.")
		return

	theBoard[char.location + move[0] + move[1]] = char.name
	theBoard[char.location] = " "
	char.location = char.location + move[0] + move[1]
	draw_board(theBoard)

game_action()