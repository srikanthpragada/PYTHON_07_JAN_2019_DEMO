fn = int(input("Enter first  number :"))
sn = int(input("Enter second number :"))

small = fn if fn < sn else sn

for i in range(2, small // 2 + 1):
    if fn % i == 0 and sn % i == 0:
        print(i)
