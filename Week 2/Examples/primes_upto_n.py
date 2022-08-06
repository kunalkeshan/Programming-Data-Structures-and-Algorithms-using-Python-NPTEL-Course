from is_prime import *

def primesupto(n):
    primeList = []
    for i in range(1, n+1):
        if is_prime(n):
            primeList += [i]
    return primeList

print(primesupto(7))