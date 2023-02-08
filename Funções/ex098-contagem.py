# Contagem
from time import sleep


def contador(inicio, fim, passo):
    print("-=" * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if inicio >= fim:
        for cont in range(inicio, fim - 1, -passo):  # para contagem regressiva
            print(f'{cont}', end=" ")  # "end" evita a quebra de linha após um espaço
            sleep(0.5)
            cont -= 1
        print("FIM!")
    else:
        for cont in range(inicio, fim + 1, passo):  # para contagem progressiva
            print(f'{cont}', end=" ")
            sleep(0.5)
            cont += 1
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print('Escolha três números para realizar uma contagem:')
n1 = int(input('Inicio:'))
n2 = int(input('Fim:'))
n3 = int(input('Passo (somente um valor positivo):'))
contador(n1, n2, n3)
escolha = str(input("Deseja realizar outra contagem? [S/N]")).strip().upper()
while escolha == "S":
    print('Escolha três números para realizar uma contagem:')
    n1 = int(input('Inicio:'))
    n2 = int(input('Fim:'))
    n3 = int(input('Passo (somente um valor positivo):'))
    contador(n1, n2, n3)
    escolha = str(input("Deseja realizar outra contagem? [S/N]")).strip().upper()
print('FIM!')
