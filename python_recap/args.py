def my_list_addition(list_arg):
    return sum(list_arg)

def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

my_list_addition([3, 5, 7, 9, 11])
my_long_method(3, 5, 7, 9, 11)

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 7, 12, 14, 55)

def what_are_args(*args):
    print(args)

def what_are_kwargs(name, job):
    print(name)
    print(job)

what_are_args(12, 34, 56)
what_are_kwargs(job="QA", name="Jose")
