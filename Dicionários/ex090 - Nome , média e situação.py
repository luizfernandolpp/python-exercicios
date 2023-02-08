# Nome, média e situação de um aluno
info = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if info['Média'] < 6:
    info['Situação'] = 'Reprovado'
else:
    info['Situação'] = 'Aprovado'
for k, v in info.items():
    print(f'{k}: {v}')



