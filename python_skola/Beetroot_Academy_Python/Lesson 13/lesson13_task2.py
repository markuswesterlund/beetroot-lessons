def myfunc():
    return myfunc2()


def myfunc2():
    print("Printing this from func2 into func")


myfunc()
