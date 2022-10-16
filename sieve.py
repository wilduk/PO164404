import math


def sieve(n):
    primes = []
    for i in range(2, n+1):
        primes.append(i)
    pierwiastek = int(math.sqrt(n))
    for i in range(2, pierwiastek+1):
        for x in range(i*2, n+1, i):
            for liczba in primes:
                if liczba == x:
                    primes.remove(liczba)
    return set(primes)


if __name__ == "__main__":
    n = 100
    print(sieve(n))
