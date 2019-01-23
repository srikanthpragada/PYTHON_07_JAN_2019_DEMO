
def process(**values):
    print( values['a'] if 'a' in values else 10)


process(x = 10, y = 20, z = 30)
process (a = 1, b = 2)


