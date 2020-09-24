def draw_board(board):

	board_line = '##############################'
	line = '------------------------------'

	print(f'{line}\n{line}', end='')

	for row in range(0, 10):
		print(f'\n{board_line}\n', end='')

		for position in range(row, row+10):
			print(f' {board[position]} |', end='')

	print(f'\n{board_line}\n{line}\n{line}')

theBoard = ['' for spaces in range(0, 100)]

draw_board(theBoard)