def power(x, n):
    # base case
    if n == 0:
        return 1
    # recursive case: n is negative
    if n < 0:
        return 1/power(x, -n)

    # recursive case: n is odd
    if n % 2 != 0:
        return power(x, n-1) * x
    else:
        n_ = n / 2
        return power(x, n_) * power(x, n_)


print(power(12, 2))


print(pow(12, 2))
