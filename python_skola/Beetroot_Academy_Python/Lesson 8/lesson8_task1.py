def oops():
    raise KeyError


def tryexc():
    x={"sweden": "stockholm", "ukraine": "kiev", "norway": "oslo"}
    try:
        # [1,2,3][4]
        x["denmark"]
    except IndexError:
        print("Index Error")
    except KeyError:
        oops()


tryexc()