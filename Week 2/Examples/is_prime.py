from factors_of_n import *

def is_prime(n):
    return(factors(n) == [1, n])

print(is_prime(8))