import random
print("Try to guess what number the computer will randomly select: ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player = input("Choose a number between 1-10: ")

if int(player) in numbers:
    computer = random.randint(1, 10)
    if player == computer:
        print("The computers number was:", computer, "and your number was:", player)
        print("You win!")
    else:
        print("The computers number was:", computer, "and your number was:", player)
        print("You lose!")
else:
    print("Sorry this game really isn't for you")
