enums = []
onums = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num % 2 == 0:
        enums.append(num)
    else:
        onums.append(num)

for n in sorted(enums) + sorted(onums):
    print(n)
