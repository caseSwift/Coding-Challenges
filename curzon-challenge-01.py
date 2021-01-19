def isCurzon(x):
    if (2**x + 1) % (2*x + 1) == 0:
        return "It is curzon"
    else:
        return "It is not curzon"


print(isCurzon(5))
