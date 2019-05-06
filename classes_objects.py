# Dictionary
lottery_player = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}

# Class
class LotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = (5, 9, 12, 3, 1, 21)

	def total(self):
		return sum(self.numbers)

# player = LotteryPlayer()
# print(player.name)
# print(player.numbers)

# # Sum (e.g.) in a dictionary
# print(sum(lottery_player['numbers']))
# # Sum (e.g.) in a class
# print(player.total())

player1 = LotteryPlayer('John')
player2 = LotteryPlayer('Rose')

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

anna = Student('Anna', 'MIT')
anna.marks.append(100)
anna.marks.append(60)
print(anna.marks)
print(anna.average())
