def bsearch(seq, v, l, r):
  if (r - l == 0):
    return(False)
  mid = (l + r) // 2
  if (v == seq[mid]):
    return (True)
  if (v < seq[mid]):
    return(bsearch(seq, v, l, mid))
  else:
    return(bsearch(seq, v, mid+1, r))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(bsearch(mylist, 1, 0, len(mylist)))