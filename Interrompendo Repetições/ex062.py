# Análise de dados
print('=-'*15)
print('Análise de dados')
print('=-'*15)
nome = str(input('Informe o nome:'))
idade = int(input('Informe a idade:'))
sexo = str(input('Informe o sexo [M/F]:')).strip().upper()
escolha = str(input('Deseja cadastrar mais alguém? [S/N]:')).strip().upper()
maioridade = 0
totalhomens = 0
mulheresvinte = 0
if escolha == "N":
    if sexo == "M" and idade >= 18:
        maioridade += 1
        totalhomens += 1
    elif sexo == "F" and idade >= 20:
        maioridade += 1
    elif sexo == "F" and idade >= 18 and idade < 20:
        maioridade += 1
        mulheresvinte += 1
elif escolha == "S":
    if sexo == "M" and idade >= 18:
        maioridade += 1
        totalhomens += 1
    elif sexo == "F" and idade >= 20:
        maioridade += 1
    elif sexo == "F" and idade >= 18 and idade < 20:
        maioridade += 1
        mulheresvinte += 1
    while True:
        nome = str(input('Informe o nome:'))
        idade = int(input('Informe a idade:'))
        sexo = str(input('Informe o sexo [M/F]:')).strip().upper()
        if sexo == "M" and idade >= 18:
            maioridade += 1
            totalhomens += 1
        elif sexo == "F" and idade >= 20:
            maioridade += 1
        elif sexo == "F" and idade >= 18 and idade < 20:
            maioridade += 1
            mulheresvinte += 1
        escolha = str(input('Deseja cadastrar mais alguém? [S/N]:')).strip().upper()
        if escolha == "N":
            break
print(f'{maioridade} pessoas possuem mais de 18 anos.')
print(f'{totalhomens} homens foram cadastrados.')
print(f'{mulheresvinte} são as mulheres cadastradas com idade abaixo de 20 anos.')
print('=-'*15)
print('FIM')
print('=-'*15)
