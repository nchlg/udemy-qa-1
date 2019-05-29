my_string = "hello, world!"
my_list = [1, 3, 5, 7, 9]

print('\n# Print string #')
for character in my_string:
	print(character)

print('\n# Print list #')
for number in my_list:
	print(number ** 2)

print('\n# Print User Wants Number #')
user_wants_number = True
while (user_wants_number == True):
	print(10)

	user_input = input('Should we print again? (y/n)')
	if (user_input) == 'n':
		user_wants_number = False
		