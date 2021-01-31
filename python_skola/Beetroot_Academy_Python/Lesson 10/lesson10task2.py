class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age


    def human_age(self):
        return self.dog_age * Dog.age_factor


a_string = Dog(5)

print("Dog age is 4. In human years it is {}".format(a_string.human_age()))

print(a_string.human_age())

