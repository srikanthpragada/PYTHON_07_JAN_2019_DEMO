def is_strong(n):
    pass

def is_prime(n):
    """
    Takes a numbers and returns true if number is prime number
    param  n: number to test
    return  : True on prime, False otherwise
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


print(is_prime.__doc__)  # Show documentation

nums = [20, 23, 57, 55, 45]
for n in nums:
    if is_prime(n):
        print(n)
