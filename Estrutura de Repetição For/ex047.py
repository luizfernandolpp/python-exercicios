# PA
a1 = int(input('Informe o primeiro termo da PA:'))
r = int(input('Informe a razão da PA:'))
a10 = a1 + (10 - 1) * r
for c in range(a1,a10 + r,r):
    print(c, end=' ')