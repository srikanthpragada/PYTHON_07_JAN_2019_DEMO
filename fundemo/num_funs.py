if __name__ == '__main__':
    print("Running num_funs module")


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
