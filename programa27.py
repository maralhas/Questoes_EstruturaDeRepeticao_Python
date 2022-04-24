from __future__ import barry_as_FLUFL
from random import betavariate


while True:
    try:
        numero_de_alunos = int(input('Informe o numero de Alunos: '))
    except:
        print('Informe só numero Inteiros.')
    else:
        print('Saiu do While 1')
        break

while True:
    try:
        numero_de_turmas = int(input('Informe o numero de Turmas: '))
        turmas = numero_de_turmas
    except:
        print('Informe só numero Inteiros.')
    else:
        print('Saiu do While 2')
        break

media_de_alunos_por_turmar = numero_de_alunos // turmas

if media_de_alunos_por_turmar > 40:
    while True:
        turmas += 1
        if media_de_alunos_por_turmar > 40:
            media_de_alunos_por_turmar = numero_de_alunos // turmas
        else:
            break

print(f'A media de alunos por turma é de {media_de_alunos_por_turmar}')
print(f'O numero de turmas iniciais: {numero_de_turmas}')
print(f'O numero total de Alunos: {numero_de_alunos}')
if (turmas - numero_de_turmas == 0 ):
    print(f'Total de turmas novas criadas para comportas os alunos {(turmas - numero_de_turmas)}')
elif (turmas - numero_de_turmas > 0 ):
    print(f'Foi criada: {(turmas - numero_de_turmas) - 1} Total de turmas {turmas -1}')