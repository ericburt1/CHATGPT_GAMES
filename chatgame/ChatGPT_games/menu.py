#


def start():
	print("Menu:")
	print("1. Tic Tac Toe")
	print("2. Password Manager")
	print("3. Text Adventure: Escape the Forest")
	print("4. Save information")

	selected_game = int(input("Please select a game to play (1, 2, or 3): "))

	if selected_game == 1:
		from chatgpt_Coding import display_board, main_game
		print("You have selected Tic Tac Toe.")
		print("\n" * 100)
		display_board()
		main_game()


	elif selected_game == 2:
		# code for Password Manager game
		print("You have selected Password Manager.")
		# code for creating, removing, and editing usernames and passwords
		print("Username and password functionality enabled.")

	elif selected_game == 3:
		from escapegame import display_title_screen
		# code for Text Adventure: Escape the Forest game
		print("You have selected Text Adventure: Escape the Forest.")
		display_title_screen()
	elif selected_game == 4:
		from savingloading import start
		print("You have selected save information.")
		start()
	else:
		print("Invalid selection. Please try again.")


start()