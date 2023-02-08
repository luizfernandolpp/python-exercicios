# Estatística de números

name: str = str(input('Informe o nome do produto:'))
price = float(input('Informe o preço do produto em R$:'))
total = 0
barato = ""
lowerprice = 0
produtomil = 0
if price > 1000:
    produtomil = produtomil + 1

escolha = str(input('Deseja inserir mais algum produto? [S/N]')).strip().upper()

if escolha == "N":
    total = total + price
    barato = name
    lowerprice = price

else:
    while escolha == "S":
        barato = name
        total = total + price
        lowerprice = price
        name = str(input('Informe o nome do produto:'))
        price = float(input('Informe o preço do produto em R$:'))
        if price > 1000:
            produtomil = produtomil + 1
        elif price < lowerprice:
            lowerprice = price
            barato = name
        escolha = str(input('Deseja inserir mais algum produto?[S/N]')).strip().upper()

print('Você gastou um total de R${:.2f}'.format(total))
print('{} produtos custam mais de R$1000.00'.format(produtomil))
print('{} foi o produto mais barato.'.format(barato))

