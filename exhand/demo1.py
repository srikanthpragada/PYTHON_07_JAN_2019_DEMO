sum = 0
while True:
    try:
        num = int(input("Enter a number [0 top stop] :"))
        if num == 0:
            break

        sum += num
    except ValueError:
        pass



print("Sum = ", sum)
