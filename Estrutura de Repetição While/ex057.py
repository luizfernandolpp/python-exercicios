# Vários valores
n = total = soma = 0
while n != 999:
    n = int(input('Escreva um número inteiro [999 para parar]:'))
    soma = soma + n
    total = total + 1
soma = soma - 999
print('Foram digitados {} números ao todo.'.format(total))
print(f'A soma de todos os {total} números é: {soma}')
