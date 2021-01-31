class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student(Person):
    def __init__(self, first_name, last_name, age, grade):
        super().__init__(first_name, last_name, age)
        self.grade = grade


class Teacher(Person):
    def __init__(self, first_name, last_name, age, pay):
        super().__init__(first_name, last_name, age)
        self.pay = pay


s = Student("Markus", "Westerlund", 28, "7b")
t = Teacher("Björn", "Barkå", 55, 5000)

print(s.first_name, s.last_name, s.age, s.grade)
print(t.first_name, t.last_name, t.age, t.pay)
