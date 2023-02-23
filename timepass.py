N = int(input())
def isprime(N):
    isprime = True

    def is_divisible(n, divisor):
        if n < (divisor - 1) * divisor:
            return False
        if n % divisor == 0:
            return True
        else:
            divisor += 1
            return is_divisible(n, divisor)

    if n == 2:
        isprime = True
    elif is_divisible(n, divisor=2):
        isprime = False
    return isprime





def getnumprimes(N):
    if n <= 2:
        return 0
    else:
        return isprime(n - 1) + getnumprimes(n - 1)