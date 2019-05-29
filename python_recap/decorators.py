import functools

def my_decorator(func):
	@functools.wraps(func)
	def function_that_runs_func():
		print("Inside the decorator!")
		func()
		print("After the decorator!")
	return function_that_runs_func

@my_decorator
def my_function():
	print("Inside the function!")

# my_function()

## Complex decorators

def decorator_with_arguments(number):
	def my_decorator(func):
		@functools.wraps(func)
		def function_that_runs_func(*args, **kwargs):
			print("Inside the decorator!")
			if (number == 56):
				print("Not running the function!")
			else:
				func(*args, **kwargs)
			print("After the decorator!")
		return function_that_runs_func
	return my_decorator

@decorator_with_arguments(55)
def my_other_function(x, y):
	print(x + y)

my_other_function(10, 20)