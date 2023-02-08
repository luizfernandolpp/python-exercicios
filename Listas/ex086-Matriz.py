# Matriz 3X3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  # Condição para estabelecer os valores de cada índice da matriz.
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]:'))
print("=" * 30)
for l in range(0, 3):     # Condição para organizar os dados em forma de uma matriz.
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")  # :^5 centraliza a formatação com 5 espaços nas laterais.
    print()
print("=" * 30)