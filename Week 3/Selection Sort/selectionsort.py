def selectionsort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start, len(l)):
            if(l[i] < l[minpos]):
                minpos = i
        (l[start], l[minpos]) = (l[minpos], l[start])
    return(l)

print(selectionsort([45, 23, 93, 92, 1, 24, 298, 2332, 38]))