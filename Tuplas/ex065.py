# tupla por extenso
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Escolha um número entre 0 e 20:'))
print(f'{tupla[n]}')
escolha = str(input('Deseja continuar? [S/N]:')).upper().strip()
if escolha == "N":
    print('FIM!')
else:
    while escolha == "S":
        n = int(input('Escolha um número entre 0 e 20:'))
        print(f'{tupla[n]}')
        escolha = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if escolha == "N":
        print('FIM!')