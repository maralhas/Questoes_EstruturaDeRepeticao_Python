print('Digite um numero negaivo para encerar com a entrada de idades: ')
contador = 0
idades = 0

while True:
    try:
        entrada = int(input('Digite uma idade: '))
    except: 
        print('Entrada de dados incorreta:')
        print('Informe um numero inteiro MAIOR que 0 para adicionar uma nova idade ou MENOR de 0 para parar a execução')
    else:
        if entrada < 0:
            break
        else:
            contador += 1
            idades += entrada

media = idades // contador

if 0 <= media <= 25:
    print(f'A média de idades é: {media}. TURMA JOVEM')
elif media <= 60:
    print(f'A média de idades é: {media}. TURMA ADULTA')
else:
    print(f'A média de idades é: {media}. TURMA IDOSA')