def product_of_prime(l, r):
    prime_product = 1

    for i in range(l, r + 1):
        if is_prime(i):
            print(i)
            prime_product = prime_product * i
    print(prime_product)


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True


product_of_prime(1, 20)
