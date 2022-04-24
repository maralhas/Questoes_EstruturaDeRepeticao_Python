alunos = []
altura = []

for i in range(10):
    aluno = int(input('Digite o numero do Aluno: '))
    aluno = altura.append(int(input("Digite a altura do aluno: ")))
    alunos.append(aluno)

indice_baixo = altura.index(min(altura))
indice_alto = altura.index(max(altura))

print(f'Aluno mais baixo é: ')
print("Aluno mais alto \n Número: ", alunos[indice_alto], "\nAltura: ", max(alunos))