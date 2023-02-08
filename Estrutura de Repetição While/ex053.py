# Fatorial
print('------ FATORIAL DE UM NÚMERO ------')
n = int(input('Informe o número:'))
c = n
fatorial = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c = c - 1
print('{}'.format(fatorial))