class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old."


a_string = Person("Markus", "Westerlund", 28)

print(a_string.talk())

