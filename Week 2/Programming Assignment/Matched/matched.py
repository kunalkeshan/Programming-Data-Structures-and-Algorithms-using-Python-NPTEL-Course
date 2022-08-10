def matched(string):
    open_list = ["("]
    closed_list = [")"]
    check = []
    for char in string:
        if char in open_list:
            check.append(char)
        elif char in closed_list:
            pos = closed_list.index(char)
            if(len(check) > 0) and (open_list[pos] == check[len(check) - 1]):
                check.pop()
            else:
                return False
    if(len(check) == 0):
        return True
    else:
        return False

print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))