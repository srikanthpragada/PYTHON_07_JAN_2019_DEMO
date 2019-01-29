a = 10


def fun():
    global a
    a = 1


fun()
print(a)
