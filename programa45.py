import os
notas = []
maior = menor = media = nota =  quant_alunos = 0
gabarito = []

print('Cadastrando o Gabarito')
for i in range(10):
    resposta = input(f'Digite a resposta da questçao {i+1}: ')
    gabarito.append(resposta.upper())
os.system('cls')

print('Responda: ')
while True:
    quant_alunos += 1
    for i in range (10):
        entrada = input('Digite a Resposta: ')
        entrada = entrada.upper()
        if gabarito[i] == entrada:
            nota += 1
    notas.append(nota)
    print(notas)
    nota = 0
    opc = input('Deseja utilizar o sistema novamente: [S]sim e [N]não: ')
    opc = opc.upper()
    if opc == 'N':
        break

maior = max(notas)
menor = min(notas)
media = sum(notas) / quant_alunos

print(f'A maior nota foi: {maior}')
print(f'A menor nota foi: {menor}')
print(f'Quantidade de Alunos: {quant_alunos}')
print(f'A media da turma é: {media}')
print('Gabarito da prova:')
for i in range (10):
    print(f'{i+1} = {gabarito[i]}')