from is_prime import *

def nprimes(n):
    (count, i, plist) = (0, 1, [])
    while(count < n):
        if is_prime(i):
            (count, plist) = (count+1, plist+[i])
        i += 1
    return(plist)

print(nprimes(10))