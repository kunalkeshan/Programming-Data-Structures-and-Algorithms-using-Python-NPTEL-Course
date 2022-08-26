from mergesorting import *

def mergesort(A, left, right):
    if right - left <=1:
        return(A[left:right])
    if right - left > 1:
        mid = (left+right)//2
        L = mergesort(A, left, mid)
        R = mergesort(A, mid, right)
    return(merge(L,R))