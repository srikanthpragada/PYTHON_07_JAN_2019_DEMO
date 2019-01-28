def positive(n):
    return n >= 0


nums = [10, -10, 20, 5, -7, 15]

for n in filter(positive, nums):
    print(n)

for n in filter(lambda v: v >= 0, nums):
    print(n)
