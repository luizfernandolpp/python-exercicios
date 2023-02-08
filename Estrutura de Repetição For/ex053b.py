# Fatorial usando For
n = int(input('Informe um número:'))
fat = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * c
print('{}'.format(fat))