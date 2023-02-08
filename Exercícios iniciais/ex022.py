# Exercício que mostra informações sobre um número:
num = int(input('Informe um número inteiro entre 0 e 9999:'))
uni = (num//1) % 10
dez = (num//10) % 10
cen = (num//100) % 10
mil = (num//1000) % 10

print('A unidade é {}'.format(uni))
print('A dezena é {}'.format(dez))
print('A centena é {}'.format(cen))
print('O milhar é {}'.format(mil))


