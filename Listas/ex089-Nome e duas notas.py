# Nome e duas notas
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])   # Adiciono nome, as duas notas e a média à lista alunos.
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while escolha != "N" and escolha != "S":      # Força o usuario a escolher entre sim (S) ou não (N).
        escolha = str(input('Escolha somente sim (S) ou não (N): ')).strip().upper()
    if escolha == "N":    # Aqui se encerra a coleta de dados.
        break
print("-=" * 50)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')     # formatações estéticas.
print("-" * 40)
for p, v in enumerate(alunos):     # formatações estéticas e exibição dos dados solicitados.
    print(f'{p:<4}{v[0]:<10}{v[2]:>8}')
print("-" * 40)
index = int(input('Informe o Nº do aluno para ver as suas notas (999 interrompe): '))
while index != 999:
    for p, v in enumerate(alunos):
        if index == p:       # Condição para exibir a nota do aluno na posição Nº.
            print(f'Notas de {v[0]} são {v[1]}')
    if index > len(alunos):  # Condição para o caso em que o usuario escolhe uma posição desocupada.
        print("O valor escolhido não corresponde a nenhum aluno.")
    print("-" * 40)
    index = int(input('Informe o Nº do aluno para ver as suas notas (999 interrompe): '))
    if index == 999:
        print("FIM")
        break





