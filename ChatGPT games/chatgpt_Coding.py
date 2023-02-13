
def display_board(board):
	print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
	print("---+---+---")
	print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
	print("---+---+---")
	print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def main_game():
	board = [" "] * 9
	turn = "X"
	while True:
		display_board(board)
		print(turn + "'s turn. Move to which place?")
		move = int(input("Enter the number (1-9): "))
		if board[move - 1] == " ":
			board[move - 1] = turn
			if turn == "X":
				turn = "O"
			else:
				turn = "X"
		else:
			print("This place is already filled. Try another.")
			continue
		if (
			(board[0] == board[1] == board[2] != " ") or
			(board[3] == board[4] == board[5] != " ") or
			(board[6] == board[7] == board[8] != " ") or
			(board[0] == board[3] == board[6] != " ") or
			(board[1] == board[4] == board[7] != " ") or
			(board[2] == board[5] == board[8] != " ") or
			(board[0] == board[4] == board[8] != " ") or
			(board[2] == board[4] == board[6] != " ")
		):
			display_board(board)
			if turn == "X":
				print("O" + " wins!\n")
			else:
				print("X wins!\n")
			break
		elif " " not in board:
			display_board(board)
			print("It's a draw!\n")
			break

print("Welcome to Tic Tac Toe!\n")
while True:
	main_game()
	play_again = input("Do you want to play again? (Y/N) ")
	if play_again.lower() == "n":
		break
print("Thanks for playing!")
from menu import start
start()