# Número primo
n = int(input('Insira um número inteiro:'))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m', end='') # cor amarela
        tot = tot + 1
    else:
        print('\033[31m', end='') # cor vermelha
    print('{} '.format(c), end='')
print('\n\033[m O número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Logo, {} é um número primo.'.format(n))
else:
    print('Logo, {} não é um número primo.'.format(n))
