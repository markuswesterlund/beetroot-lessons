import json

employee_list = []


class Employee:
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@example.com'
        self.number = number


    def fullname(self):
        return "{} {}".format(self.first, self.last)


def save_employee():
    with open("employees.json", "w") as f:
        data = json.dumps(employee_list, indent=2)
        f.write(data)


f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
c_number = input("Enter phone number: ")

emp_info = Employee(f_name, l_name, c_number)
full_info = {"First name": f_name, "Last name": l_name,
             "Full name": emp_info.fullname(), "Phone Number": c_number,
             "Email": emp_info.email}

employee_list.append(full_info)
save_employee()
print("Contact added to employees.json")
