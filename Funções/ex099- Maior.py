# Maior dentre vários valores
from time import sleep


def maior(*valores):
    print("-=" * 20)
    print("Analisando os valores passados...")
    greater = 0
    for num in valores:
        print(num, end=" ")
        sleep(0.3)
        if num > greater:  # filtragem do maior valor.
            greater = num
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {greater}.')


maior(1, 0, 1, 9, 1, 7)
maior(1,9,9,6)
maior(0,7,0,3)
