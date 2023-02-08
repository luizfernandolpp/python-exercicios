# Listas pares e impares versao do Guanabara.
numeros = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print("=" * 50)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')
print("=" * 50)