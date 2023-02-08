# Soma de múltiplos ímpares de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores ímpares e múltiplos de três entre 1 e 500 é {}.'.format(cont,soma))
