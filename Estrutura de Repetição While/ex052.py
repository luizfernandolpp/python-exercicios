# Menu de opções
print('------ MENU DE OPÇÕES ------')
a = int(input('Informe um número:'))
b = int(input('Informe outro número:'))
menu = 0
while menu < 5:
    print('Somar: 1' , 'Multiplicar: 2', 'Maior: 3', 'Novos números: 4', 'Sair: 5')
    menu = int(input('Escolha uma opção:'))
    if menu == 1:
        soma = a + b
        print('A soma é {}.'.format(soma))
    elif menu == 2:
        multiplicar = a * b
        print('A multiplicação é {}.'.format(multiplicar))
    elif menu == 3 and a >= b:
        maior = a
        print('O maior número é {}.'.format(maior))
    elif menu == 3 and b >= a:
        maior = b
        print('O maior número é {}.'.format(maior))
    elif menu == 4:
        a = int(input('Informe um novo número:'))
        b = int(input('Informe outro número:'))
print('------ FIM ------')

