#Zadanie 1
# a)
"""
def nwd(a,b):
    if a == b:
        return a
    elif a > b:
        a = a-b
    else:
        b = b-a
    return a

print(nwd(3,2))
    """


def nwd1(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

print(nwd1(2,1))


# b)
def nwd2(a,b):
    if a!=b:
        return nwd2(a-b,b)
    else:
        return nwd2(a,b-a)
    

print(nwd2(2,1))


def nwdRekII(a,b):
    if b!=0:
        return nwdRekII(b, a%b)
    return a
