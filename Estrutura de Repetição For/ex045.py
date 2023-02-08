# Tabuada.
n = int(input('Informe o número no qual você deseja calcular a tabuada:'))
print('A tabuada de {} é:'.format(n))
for c in range(0,11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
