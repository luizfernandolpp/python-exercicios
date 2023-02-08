# PA usando While
a1 = int(input('Informe o primeiro termo da PA:'))
r = int(input('Informe a razão da PA:'))
c = 0 # contador para usar no while
print('Os dez primeiros termos desta PA são:', end=' ')
while c < 10:
    print('{} → '.format(a1) if c < 9  else '{}'.format(a1), end= ' ')
    a1 = a1 + r
    c = c + 1
