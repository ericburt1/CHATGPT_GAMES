import os
def start():
	print("Welcome to a saving and loading information test.")
	print("What would you like to do?")
	print("1. Save")
	print("2. Load")
	print("3. Erase")
	print("4. Quit")
	option = int(input("What do you want to do?\n"))
	if option == 1:
		save()
	if option == 2:
		load()
	else:
		quit()





def save():
	# Specify the file to delete
	name = input("Enter your name.\n")
	age = input("Enter your age.\n")
	email = input("Enter your email.\n")

	# Open a file for writing
	with open("information.txt", "w") as file:
		# Write the information to the file
		file.write(f"Name: {name}\n")
		file.write(f"Age: {age}\n")
		file.write(f"Email: {email}\n")

	print("Information saved to file.")
	start()

def load():
	# Open the file for reading
	with open("saved_data.txt", "r") as file:
		# Read the lines of the file into a list
		lines = file.readlines()

	# Initialize an empty dictionary to store the data
	data = {}

	# Loop through each line in the file
	for line in lines:
		# Split the line into key-value pairs on the first colon
		key, value = line.split(":", 1)
		# Strip whitespace from the key and value
		key = key.strip()
		value = value.strip()
		# Convert the value to a number if possible
		if value.isdigit():
			value = int(value)
		# Add the key-value pair to the dictionary
		data[key] = value

	# Print the loaded data to the console
	print(data)
	start()

start()