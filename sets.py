unique_numbers = {1, 5, 6}
print(type(unique_numbers))
print(unique_numbers)
unique_numbers.add(2)
unique_numbers.add(3)
unique_numbers.add(1)
unique_numbers.add(4)
print(unique_numbers)

list_numbers = [1, 2, 5, 30, 3, 2, 5, 6]
list_numbers = list(set(list_numbers))
print(list_numbers)

# print(dir(unique_numbers)) kolla vilka kommandon som funkar på sets etc.

new_list = [1] * 100
print(new_list.count(1))

list_a = ["a", "b", "c"]
list_b = ["d", "e"]
list_a += list_b
print(list_a)

set_a = {"1", "2", "3"}
set_b = {"2", "3", "4"}
for n in set_a:
    if n in set_b:
        print("These elements are in both sets =", set_b.intersection(set_a))
        break
    else:
        print("No elements were the same in the sets.")
        break

name = "markus"
letters = list(name)
print(name)
print(letters)
print("".join(letters))


