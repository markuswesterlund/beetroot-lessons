import random
a_list1 = []
a_list2 = []
a_check_list = []
i = 0
while i < 10:
    i += 1
    a_list1.append(random.randrange(1, 11))
    a_list2.append(random.randrange(1, 11))
    n = 0
    while n < 10:
        n += 1
        if n in a_list1 and n in a_list2 and n not in a_check_list:
            a_check_list.append(n)
print(a_list1)
print(a_list2)
print("Numbers that were in both lists:", a_check_list)
