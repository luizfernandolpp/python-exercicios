# PA melhorada
a1 = int(input('Informe o primeiro termo da PA:'))
r = int(input('Informe a razão da PA:'))
c = 0 # contador para os termos da PA
total = 0 # contador do total de termos
extra = 10 # extra a partir do décimo termo da PA de acordo com o problema inicial.
print('Os dez primeiros termos de uma PA de razão {} são:'.format(r))
while extra != 0:
    total = total + extra
    while c < total:
        print('{} →'.format(a1), end=' ')
        a1 = a1 + r
        c = c + 1
    print('PAUSA')
    extra = int(input('Você deseja inserir mais algum termo à PA? Se sim, quantos?'))
print('Foram contabilizados {} termos.'.format(total))
