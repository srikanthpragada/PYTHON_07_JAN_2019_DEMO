# Takes a number on command line and displays whether it is prime number

import sys
import num_funs

num = int(sys.argv[1])

if num_funs.is_prime(num):
    print(f"{num} is a prime number!")
else:
    print(f"{num} is NOT a prime number!")

