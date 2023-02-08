# Valores únicos e em ordem crescente (versão simplificada)
Valores = []
while True:
    n = int(input('Digite um valor:'))
    if n not in Valores:
        Valores.append(n)
        print('Valor adicionado à lista.')
    else:
        print('Este valor já foi escolhido e não será adicionado.')
    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()
    while escolha != "N" and escolha != "S":
        escolha= str(input('Escolha somente entre sim ou não [S/N]:')).strip().upper()
    if escolha == "N":
        break
Valores.sort()
print(f'Você digitou os seguintes valores: {Valores}')