from math import *


def intreverse(num):
    intreversed_num = 0
    count_num = num
    count = 0
    tens = 1
    while(count_num != 0):
        count += 1
        count_num //= 10
    for i in range(1, count):
        tens *= 10
    while(num != 0):
        rmnd = floor(num%10)
        intreversed_num += rmnd*tens
        tens /= 10
        num = num//10
    return floor(intreversed_num)

print(intreverse(3))
