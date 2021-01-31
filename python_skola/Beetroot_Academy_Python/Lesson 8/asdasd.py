import random
# Numbers: 1 2 2.3
# Booleans: True/False
# Nothing: None
# Lists: [], (1,), {1,2}
# Dicts: {"a": "b"}

contacts = ["Contact 1", "Contact 2", "Contact 3"]

print("While loop:")
i = 0
while i < len(contacts):
    print(i+1, ":", contacts[i])
    i += 1

print("\nFor Loop:")
for contact in contacts:
    print("Contact:", contact)

print("\nFunction:")


def main():
    print("Hello, world!")
    return random.choice([True, False])


ok = main()
if not ok:
    print("Main failed!")
else:
    print("All done!")


a_list = ["Hello", ["World"]]
print(a_list[2])


a_dict = {"a": "b"}
print(a_dict["c"])