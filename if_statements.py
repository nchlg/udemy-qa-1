# known_people = ['John', 'Anna', 'Jacqueline']
# person = input('Enter the person you know: ')
# if person in known_people:
# 	print('You know {}'.format(person))
# else:
# 	print('You don\'t know {}'.format(person))

## Exercise

def who_do_you_know():
	# Ask the user for a list of people they know
	# Split the string into a list
	# Return list
	names = input('Who do you know? (Please, separate the names with a comma.) ') # bob, laura, donna
	return string_to_list_of_names(names)

def ask_user(names):
	# Ask user for a name
	# See if the name is in the list of people
	# Print out that they know the person
	name = input('Insert a name: ').title() # dale -> Dale
	if name in names:
		print('You know {}'.format(name))
	else:
		print('You don\'t know {}'.format(name))

def string_to_list_of_names(names_string):
	names_list = names_string.replace(' ', '').split(',')
	names_list = list(map(lambda x: x.title(), names_list)) # ['Bob', 'Laura', 'Donna']
	return names_list


people_you_know = who_do_you_know()
print(people_you_know)
ask_user(people_you_know)
