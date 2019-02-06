sum = 0
while True:
    try:
        num = int(input("Enter a number [0 top stop] :"))
        if num == 0:
            break

        sum += num
    except Exception as ex:
        pass



print("Sum = ", sum)
