# Lista ordenada em ordem decrescente; quantos valores aparecem?; o valor 5 foi digitado?
lista = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    escolha = str(input('Deseja inserir outro valor? [S/N]')).strip().upper()
    while escolha != "N" and escolha != "S":     # Condição que obriga o usuario a escolher somente entre S ou N.
        escolha = str(input('Digite somente sim ou não [S/N]:')).strip().upper()
    if escolha == "N":   # Encerra o programa caso o usuario escolha a opção N.
        break

lista.sort(reverse=True)  # Coloca a lista final em ordem decrescente.

print("=" * 30)
print(f'Ao todo, foram digitados {len(lista)} valores.')
print(lista)
if 5 in lista:        # Condição para informar se o número 5 está presente na lista final.
    print(f'O valor 5 está presente na lista.')
else:
    print(f'O valor 5 não estã presente na lista.')
print("=" * 30)
