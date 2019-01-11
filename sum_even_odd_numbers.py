# print sum of even numbers and odd numbers
even_sum = odd_sum = 0

for i in range(1, 6):
    num = int(input("Enter a number :"))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(even_sum, odd_sum)
