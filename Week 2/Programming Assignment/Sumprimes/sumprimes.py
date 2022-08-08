def factors(num): 
    factorsList = []
    for i in range(1, num+1):
        if(num%i) == 0:
            factorsList.append(i)
    return factorsList

def isPrime(num):
    return factors(num) == [1, num]


def sumprimes(list):
    total = 0
    for i in list:
        if(isPrime(i)):
            total += i
    return total


print(sumprimes([-3,1,6]))

