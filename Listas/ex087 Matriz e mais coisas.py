# Informações sobre dados de uma matriz 3X3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma3 = 0
for line in range(0, 3):
    for col in range(0, 3):
        matriz[line][col] = int(input(f'Digite o valor [{line}, {col}] da matriz:'))
        if matriz[line][col] % 2 == 0:  # Condição para encontrar os valores pares.
            pares += matriz[line][col]
        if matriz[line][col] == matriz[line][2]:  # Condição para somar os valores da terceira coluna.
            soma3 += matriz[line][2]
maior2 = max(matriz[1])   # O maior valor da segunda linha.

print("=" * 30)
for line in range(0, 3):   # Condição para formatação usual de uma matriz.
    for col in range(0, 3):
        print(f'[{matriz[line][col]:^5}]', end="")
    print()
print("=" * 50)
print(f'A soma de todos os valores pares digitados é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior2}.')
print("=" * 50)