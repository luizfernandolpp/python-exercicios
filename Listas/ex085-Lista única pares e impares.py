# Filtragem de pares e ímpares em uma lista composta
numeros = []
pares = []
impares = []
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor:'))
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()

numeros.append(pares)
numeros.append(impares)
print("=" * 50)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')
print("=" * 50)
