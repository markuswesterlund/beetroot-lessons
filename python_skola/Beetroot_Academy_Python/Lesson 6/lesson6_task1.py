words = input("Enter string here:").split()
a_dict = dict()
for w in words:
    if w in a_dict:
        a_dict[w] += 1
    else:
        a_dict[w] = 1
print(a_dict)
