def Fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return Fibbo(n-1) + Fibbo(n-2)


n = int(input())
print(Fibbo(n))
