
def collision_detected(board, piece):
	for j in range(5):
		for i in range(5):
			if piece.matrix[j][i]:
				if board.matrix[j + piece.y][i + piece.x]: return True

	return False

def add_to_board(board, piece):
	for j in range(5):
		for i in range(5):
			if piece.matrix[j][i]:
				board.matrix[j + piece.y][i + piece.x] = 1
				