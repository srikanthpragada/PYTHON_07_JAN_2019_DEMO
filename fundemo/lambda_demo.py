def abs(n):
    return n if n >= 0 else n * -1


nums = [10, -10, 20, 5, -7, 15]

for n in sorted(nums, key=lambda v: v if v >= 0 else v * -1):
    print(n)


