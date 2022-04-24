while True:
    nome = input('Digite seu nome: ')
    if len(nome) >= 3:
        break
    else:
        print('ERRO!!! O nome deve ter mais de 3 caracteres.')
while True:
    try:
        idade = int(input('Digite sua idade: '))
        if  0 < idade < 150:
            break
        else:
            print('Idade deve ser mair que 0 e menor 150')
    except ValueError:
        print('Entrada invalida! Digite apenas numeros inteiros.')
while True:
    try:
        salario = float(input('Digite seu salário: '))
        if salario > 0:
            break
        else:
            print('Salário deve ser maior que 0,00')
    except ValueError:
        print('Entrada invalida! Digite apenas numeros.')
while True:
    sexo = input('Informe seu sexo (F) Feminino ou (M) pata Masculino: ')
    sexo = sexo.upper()
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print('Erro!!! - Digite (F) Feminino ou (M) pata Masculino')
while True:
    estado_civil = input('Informe seu estado civil: [S]solteiro(a), [C]casado(a), [V]viuvo(a) ou [D]divorciado(a)')
    estado_civil = estado_civil.upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        break
    else:
        print('Erro!!! - Informe: [S]solteiro(a), [C]casado(a), [V]viuvo(a) ou [D]divorciado(a)')