def cuadrado(n):
    print (n**2)
    return (n**2)
l = [4,6,8]
l2 = map(cuadrado, l)
resultado =list(l2)
print (l2)