# Listagem com nomes e pessoas mais leves e mais pesadas
dados = []
pessoa = []
maior = menor = 0
nomemaior = []
nomemenor = []
while True:
    pessoa.append(str(input('Nome:')))
    pessoa.append(float(input('Peso:')))
    if len(dados) == 0:   # A lista pessoa só tem um cadastro, logo o maior peso = menor peso.
        maior = menor = pessoa[1]
    else:                # A lista dados já possui um cadastro.
        if pessoa[1] > maior:   # Condição para estipular o maior valor.
            maior = pessoa[1]
        if pessoa[1] < menor:   # Condição para estipular o menor valor.
            menor = pessoa[1]
    dados.append(pessoa[:])     # Cria uma cópia da lista pessoa e adiciona à lista dados
    pessoa.clear()              # Limpa a lista pessoa.
    escolha = str(input('Deseja cadastrar mais alguém? [S/N]')).strip().upper()
    while escolha != "N" and escolha != "S":     # Força o usuario a escolher entre sim (S) ou não (N).
        escolha = str(input('A resposta deve ser sim ou não [S/N]:')).strip().upper()
    if escolha == "N":     # Fornece o total de pessoas cadastradas, o maior peso e o menor peso.
        break

for peso in dados:         # Condições para filtrar os usuarios que possuem o maior peso e o menor peso.
    if peso[1] == maior:
        nomemaior.append(peso[0])
    if peso[1] == menor:
        nomemenor.append(peso[0])

print("=" * 30)
print(f'Ao todo, {len(dados)} pessoas foram cadastradas.')
print(f'O maior peso cadastrado foi {maior}kg. Pessoas com este peso: {nomemaior}')
print(f'O menor peso cadastrado foi {menor}kg. Pessoas com este peso: {nomemenor}')
print("=" * 30)




