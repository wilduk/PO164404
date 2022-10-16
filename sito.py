import math


def sito(primes):
    n = int(input())
    primes.clear()
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
    primes = []
    print(sito(primes))
