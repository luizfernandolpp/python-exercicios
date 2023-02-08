# Maior  valor, menor valor e a media
n = int(input('Digite um número:'))
maior = menor = media = soma = total = 0
resposta = str(input('Deseja continuar? [S/N]')).strip().upper()
if resposta == "N":               # caso o usuário não queira continuar.
    maior = menor = media = soma = n
    total = 1
    print('Você digitou {} número. A média dele é {}.'.format(total, media))
    print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
elif resposta == "S":            # caso o usuário queira continuar.
    maior = menor = n            # tanto maior como menor recebem o primeiro número inserido pelo usuário.
    soma = n             # a soma também recebe o primeiro número inserido pelo usuário para que ele seja contabilizado.
    total = 1                    # o total inclui o primeiro número inserido pelo usuário.
    n = int(input('Digite um número:'))      # o usuário insere o segundo número.
    total = total + 1
    soma = soma + n
    media = soma / total
    if n >= maior:
        maior = n
    elif n <= maior:
        menor = n
    resposta = str(input('Deseja continuar? [S/N]')).strip().upper()
    while resposta == "S":          # se repete enquanto o usuário digitar "s" ou "S".
        n = int(input('Digite um número:'))
        total = total + 1
        soma = soma + n
        media = soma / total
        if n >= maior:
            maior = n
        elif n <= maior:
            menor = n
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()

    print('Você digitou {} números. A média deles é {}.'.format(total, media))
    print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
print('------ FIM ------')
