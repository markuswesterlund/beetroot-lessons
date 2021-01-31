letters = "1337"
numbers = []
for letter in letters:
    number = chr(letter) - 96
    numbers.append(number)
print(numbers)