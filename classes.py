class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

# anna = Student("Anna", "Oxford")
# friend = anna.friend("Greg")
# print(friend.name)
# print(friend.school)

anna = WorkingStudent("Anna", "Oxford", 20.00)
friend = WorkingStudent.friend(anna, "Greg", 17.50)
print(anna.salary)
print(friend.name)
print(friend.school)
print(friend.salary)
