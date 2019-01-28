def process(n1, n2, op):
    print(op(n1, n2))


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


process(10, 20,lambda x,y : x + y)
process(10, 20, mul)
