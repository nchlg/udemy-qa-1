# Variables

a = 5
string_variable = "hello"
string_quotes = 'hello'

# print(a);

# Methods

def my_print_method(my_argument):
	print(my_argument)

def my_multiply_method(number_one, number_two):
	result = number_one * number_two
	return str(number_one) + ' * ' + str(number_two) + ' = ' + str(result)

my_print_method('Hello, world!')
print(my_multiply_method(12, 3))

