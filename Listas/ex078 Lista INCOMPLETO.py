# Lista maior menor e posição
print("=" * 35)
print('Maior, menor e posição em LISTAS.')
print("=" * 35)
lista = []

for c in range(0, 5):  # Criando a lista
    num = int(input('Digite um número:'))
    lista.append(num)

print(f'A sua lista é: {lista}')

# Maior valor e sua/suas posição/posições.

maior = max(lista)  # O maior valor presente na lista.
listpos = []  # Lista a ser preenchida com as posições do maior valor na lista de números inseridos.

for pos, valor in enumerate(lista):  # Filtro para determinar as posições do maior valor na lista.
    if valor == maior:
        listpos.append(pos)

ocorrencia = lista.count(maior)  # verifica a ocorrência do maior valor

if ocorrencia == 1:
    print(f'O maior valor da lista é {maior} e se encontra na posição {lista.index(maior)}.')
else:
    print(f'O maior valor da lista é {maior} e se encontra nas posições', end=" ")
    for i in listpos:  # separa as posições por vírgulas (melhor que # consegui com o que sei até agora)
        print(f'{i}', ',' if i < len(listpos) else '.', end=' ')

# Menor valor e sua/suas posição/posições.

menor = min(lista)  # O menor valor presente na lista.
listposmenor = []  # Lista a ser preenchida com as posições do menor valor na lista de números inseridos.

for pos, valor in enumerate(lista):  # Filtro para determinar as posições do menor valor na lista.
    if valor == menor:
        listposmenor.append(pos)

ocorrenciamenor = lista.count(menor)  # Verifica a ocorrência do menor valor.

if ocorrenciamenor == 1:
    print(f'\n O menor valor da lista é {menor} e se encontra na posição {lista.index(menor)}.')
else:
    print(f'\n O menor valor da lista é {menor} e se encontra nas posições', end=' ')
    for i in listposmenor:
        print(f'{i}', ',' if i <= len(listposmenor) else '.', end=' ')
