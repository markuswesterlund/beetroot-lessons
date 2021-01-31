import random
word = input("Enter your word here: ")
i = 0
while i < 5:
    i += 1
    print("".join(random.sample(word, len(word))))
