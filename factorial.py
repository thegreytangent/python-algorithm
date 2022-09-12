
def not_factorial(n):
    product = 1
    while n > 0:
        product *= n
        n = n - 1
    return product


def factorial(n):
    if n == 0:
        return 1;
    return n * factorial(n-1)


print(factorial(5))
