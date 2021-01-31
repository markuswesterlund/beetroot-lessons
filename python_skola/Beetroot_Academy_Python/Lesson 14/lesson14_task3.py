"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):

    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

"""


def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def inner(*args, **kwargs):

            if len(args[0]) > max_length:
                print(f" {args[0]} is too long")
                return False

            elif not isinstance(args[0], type_):
                print(f"{args[0]} is not the correct type")
                return False

            for item in contains:
                if item not in args[0]:
                    print("items in list not used")
                    return False

            result = func(*args, **kwargs)
            return result

        return inner

    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
