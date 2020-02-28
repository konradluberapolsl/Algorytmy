from  Stack import Stack
def read(name):
    file = open(name, "r")
    list = file.read().splitlines()
    file.close()
    return list


def ONP(list):
    Stos= Stack()
    for item in list:
        for char in item:
            pass
