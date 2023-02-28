def isit(x):
    y=str(x)
    yes=0
    magic=int(len(y)/2)
    for i in range(magic):
        if (y[i]==y[len(y)-i-1]):
            continue
        else :
            return False
    return True

num=-10101
print(isit(num))