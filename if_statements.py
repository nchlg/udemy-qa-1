known_people = ['John', 'Anna', 'Jacqueline']
person = input('Enter the person you know: ')
if person in known_people:
	print('You know {}'.format(person))
else:
	print('You don\'t know {}'.format(person))

