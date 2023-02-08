# Valores únicos e em ordem crescente (versão complicada de um programador iniciante)
Valores = []
n = int(input('Digite um valor:'))
Valores.append(n)
print('Valor foi adicionado à lista')
escolha = str(input('Deseja inserir outro valor? [S/N]')).strip().upper()

while escolha != "N" and escolha != "S":   # O usuario deve escolher entre S ou N.
    escolha = str(input('Por favor, escolha somente entre sim ou não [S/N]:')).strip().upper()
if escolha == "N":
    print("=" * 30)
    print(f'Você digitou os seguintes valores: {Valores}')    # Caso o usuario escolha N, o programa se encerrará aqui.
    print("=" * 30)
elif escolha == "S":
    novo = int(input('Digite um valor:'))    # O usuario escolhe S e insere um novo valor.
    while novo == n:                            # Condições para o caso do novo valor ser igual ao primeiro inserido.
        print(f'Este valor já foi escolhido e não será adicionado.')
        novo = int(input('Digite um valor:'))
    Valores.append(novo)         # Adiciona um novo valor à lista.
    print('Valor foi adicionado à lista.')
    escolha = str(input('Deseja inserir outro valor? [S/N]')).strip().upper()
    while escolha != "N" and escolha != "S":  # O usuario deve escolher entre S ou N.
        escolha = str(input('Por favor, escolha somente entre sim ou não [S/N]:')).strip().upper()
    while escolha == "S":      # Enquanto o usuario quiser continuar.
        novo = int(input('Digite um valor:'))
        for c in Valores:      # Checa se o novo valor já está na lista.
            if novo == c:
                print(f'Este valor já foi escolhido e não será adicionado.')
                novo = int(input('Digite um valor:'))
                while novo == c:   # Enquanto o usuario inserir um valor que já esteja na lista.
                    print(f'Este valor já foi escolhido e não será adicionado.')
                    novo = int(input('Digite um valor:'))
        Valores.append(novo)    # Adiciona um novo valor à lista
        print('Valor foi adicionado à lista.')
        escolha = str(input('Deseja inserir outro valor? [S/N]')).strip().upper()
        while escolha != "N" and escolha != "S":  # O usuario deve escolher entre S ou N.
            escolha = str(input('Por favor, escolha somente entre sim ou não [S/N]:')).strip().upper()

    Valores.sort()      # Ordena a lista final.
    print("=" * 30)
    print(f'Você digitou os seguintes valores: {Valores}')      # O programa se encerra aqui.
    print("=" * 30)