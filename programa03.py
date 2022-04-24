validador = 0
while validador != 5:
    nome = input('Digite seu nome: ')
    if  len(nome) >= 3:
        validador += 1
    else:
        print('Erro!!! - Nome deve conter mais de três letras:')
    
    idade = int(input('Informe sua Idade: '))
    if 150 < idade > 0:
        validador += 1
    else:
        print('Erro!!! - Idade inválido:')
    
    salario = float(input('Infor o salário: '))
    if salario > 0:
        validador += 1
    else:
        print('Erro!!! - Salário inválido:')
    
    sexo = input('Informe seu sexo (F) Feminino ou (M) pata Masculino')
    sexo = sexo.upper()
    if sexo == 'F' or sexo == 'M':
        validador += 1
    else:
        print('Erro!!! - Sexo inválido:')

    estado_civil = input('Informe seu estado civil: [S]solteiro(a), [C]casado(a), [V]viuvo(a) ou [D]divorciado(a)')
    estado_civil = estado_civil.upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        validador += 1
    else:
        print('Erro!!! - Estado Cicil inválido:')

