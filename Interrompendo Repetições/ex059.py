# Vários valores até 999.
print('------ CONTAGEM ------')
n = soma = total = 0
while True:
    n = int(input('Digite um número. [999] para parar:'))
    if n == 999:
        break
    else:
        soma = soma + n
        total = total + 1
print(f'A soma dos {total} números digitados é {soma}.')
print('------ FIM ------')