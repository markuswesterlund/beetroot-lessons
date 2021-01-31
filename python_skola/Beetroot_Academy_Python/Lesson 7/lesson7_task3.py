def make_operation(op, *args):
    result = 0
    if op == "+":
        for num in args:
            result += num
    elif op == "-":
        for num in args:
            result -= num
    elif op == "*":
        result = 1
        for num in args:
            result *= num
    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))