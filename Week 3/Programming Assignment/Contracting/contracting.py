def contracting(l):
  for z in range(0,len(l)-3):
    A=abs(l[z+2]-l[z+1])
    B=abs(l[z+1]-l[z])
    if A<B:
      continue
    else:
      return (False) 
  return (True)

print(contracting([9,2,7,3,1]))