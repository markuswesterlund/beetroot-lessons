#print("".join(random.sample(word, len(word))))
#print("".join(random.sample(word, len(word))))
#print("".join(random.sample(word, len(word))))
#print("".join(random.sample(word, len(word))))
#print("".join(random.sample(word, len(word))))

#i = 0
#while i < 5:
#    print("".join(random.sample(word, len(word))))
#    i += 1

# for _ in range(5):
#     print("".join(random.sample(word, len(word))))

# while n < 10:
#     n += 1
#     if n in a_list1 and n in a_list2 and not n in a_check_list:
#         a_check_list.append(n)
import random
word = input("Enter your word here: ")
i = 0
while i < 5:
    i += 1
    print("".join(random.sample(word, len(word))))