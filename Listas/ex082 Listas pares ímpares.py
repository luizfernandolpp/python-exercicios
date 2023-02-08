# Listas pares e ímpares
Lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor:'))
    Lista.append(n)
    Lista.sort()     # Organiza a lista total em ordem crescente.
    if n % 2 == 0:   # Condição para ver se n é par.
        par.append(n)
        par.sort()     # Organiza a lista par em ordem crescente.
    else:          # Se n é ímpar.
        impar.append(n)
        impar.sort()     # Organiza a lista ímpar em ordem crescente.
    escolha = str(input('Deseja outro valor? [S/N]:')).strip().upper()
    while escolha != "N" and escolha != "S":   # Força o usuario a escolher entre sim ou não [S/N].
        escolha = str(input('Escolha somente entre sim ou não [S/N]:')).strip().upper()
    if escolha == "N":      # Encerra o programa.
        break

print("=" * 30)
print(f'Lista final: {Lista}')
print(f'Lista com os elementos pares: {par}')
print(f'Lista com os elementos ímpares: {impar}')
print("=" * 30)
