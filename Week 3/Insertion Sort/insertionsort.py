def insertionsort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos - 1]:
            (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
            pos = pos - 1
    return(seq)

print(insertionsort([45, 42, 23, 9, 23, 98, 12, 23, 57]))
