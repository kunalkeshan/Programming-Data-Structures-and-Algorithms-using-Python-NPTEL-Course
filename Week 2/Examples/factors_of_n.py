def factors(n):
    factorsList = []
    for i in range(1, n+1):
        if(n%i) == 0:
            factorsList.append(i)
    return factorsList

print(factors(5))