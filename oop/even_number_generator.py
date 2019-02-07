def even_numbers(start, end):
    start = start if start % 2 == 0 else start + 1
    for n in range(start, end + 1, 2):
        yield n


g = even_numbers(10, 15)
print(next(g))

for n in g:
    print(n)
