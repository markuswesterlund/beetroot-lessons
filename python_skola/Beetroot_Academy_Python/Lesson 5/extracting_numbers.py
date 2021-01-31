a_list = list(range(1, 101))
b_list = []
i = 0
while i < 101:
    i += 1
    if i % 7 == 0 and not i % 5 == 0:
        b_list.append(i)
print(b_list)
