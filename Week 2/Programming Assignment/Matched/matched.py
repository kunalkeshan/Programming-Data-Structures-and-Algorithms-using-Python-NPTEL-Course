def matched(string):
    isMatched = True
    for i in range(0, len(string)):
        if(string[i] == "("):
            print(-i-1, string[-i-1])
        elif(string[i] == ")"):
            print(-i-1, string[-i-1])
    return isMatched

print(matched("(7)(a"))