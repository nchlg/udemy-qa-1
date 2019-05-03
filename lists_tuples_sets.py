grades = [77, 80, 60, 90, 30]
tuple_grades = (77, 80, 60, 90, 30) # imutable
set_grades = {77, 80, 60, 90, 30} # unique & unordered

# List increasing
grades.append(100)
# print(grades)
# Tuple increasing
tuple_grades = tuple_grades + (100,)
# print(tuple_grades)
# Set increasing
set_grades.add(100)
# print(set_grades)

# Accessing and changing values
grades[0] = 78
# print(grades)
# Can't be done with tuples nor sets
# tuple_grades[0] = 78
# set_grades[0] = 78

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers
	.intersection(winning_numbers))

print(your_lottery_numbers
	.union(winning_numbers))

print(your_lottery_numbers
	.difference(winning_numbers))
