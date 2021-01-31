import random
a_list = []
i = 0
while i < 10:
    i += 1
    a_list.append(random.randrange(1, 101))
sorted_list = sorted(a_list)
print(a_list)
print(sorted_list)
print("Highest number:", max(a_list))