# Lista ordenada usando insert
valores = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > valores[-1]:  # Condição para o primeiro valor inserido e para o maior valor inserido.
        valores.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):     # Varredura dos elementos adicionados na lista até então.
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado à posição {pos} da lista.')
                break
            pos += 1

print("=" * 25)
print(f'Você digitou os seguintes valores: {valores}')
print("=" * 25)