def factors(num): 
    factorsList = []
    for i in range(1, num+1):
        if(num%i) == 0:
            factorsList.append(i)
    return factorsList

def isPrime(num):
    return factors(num) == [1, num]


def sumprimes(list):
    sumList = []
    for i in list:
        if(isPrime(i)):
            sumList.append(i)
    return sum(sumList)


print(sumprimes([-3,1,6]))

