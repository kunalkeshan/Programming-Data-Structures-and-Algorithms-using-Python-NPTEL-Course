def leftrotate(m):
    ans=list()
    for a in range(len(m)):
        ans.append([])
        for b in range(len(m)):
            ans[a].append(m[b][len(m)-a-1])
    return(ans) 