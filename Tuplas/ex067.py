# numeros aleatórios e tuplas
import random
numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(numeros)
ordenados = sorted(numeros)
print(f'Os números gerados são:{ordenados}.')
print(f'O maior número dessa lista é {(ordenados[4])}.')
print(f'O menor número dessa lista é {(ordenados[0])}.')


