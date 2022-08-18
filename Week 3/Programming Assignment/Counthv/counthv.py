def counthv(l):
  hill_count,valley_count=0,0
  if len(l)>2:
    for i in range(1,len(l)-1):
      if l[i]>l[i-1] and l[i]>l[i+1]:
        hill_count+=1
      elif l[i]<l[i-1] and l[i]<l[i+1]:
        valley_count+=1
  return ([hill_count,valley_count])