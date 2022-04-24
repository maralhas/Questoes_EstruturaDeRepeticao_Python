repetir = 'Repetir'
while repetir == 'Repetir':
    while True:
        try:
            populacao_a = int(input('Digite a população do mais A: '))
            break
        except ValueError:
            print('Você deve apenas informar números inteiros: ')
    while True:
        try:
            populacao_b = int(input('Digite a população do mais B: '))
            break
        except ValueError:
            print('Você deve apenas informar números inteiros: ')
    while True:
        try:
            taxa_de_crescimento_de_a  = float(input('Digite a taxa de crescimento do país A:  '))
            taxa_de_crescimento_de_a = (taxa_de_crescimento_de_a / 100) + 1
            break
        except ValueError:
            print('Você deve apenas informar números inteiros: ')
    while True:
        try:
            taxa_de_crescimento_de_b  = float(input('Digite a taxa de crescimento do país A:  '))
            taxa_de_crescimento_de_b = (taxa_de_crescimento_de_b / 100) + 1
            break
        except ValueError:
            print('Você deve apenas informar números inteiros: ')
    anos = 0

    while populacao_a < populacao_b:
        anos += 1
        populacao_a *= taxa_de_crescimento_de_a
        populacao_a = int(populacao_a)
        populacao_b *= taxa_de_crescimento_de_b
        populacao_b = int(populacao_b)

    print(f'População no ano {anos}')
    print(f'População de A: {populacao_a}')
    print(f'População de {populacao_b}')

    while True:
        repetir = input('Deseja repitir a operação: [S]Sim ou [N]não: ')
        repetir = repetir.upper()
        if repetir == 'S':
            repetir = 'Repetir'
            break
        elif repetir == 'N':
            repetir = 'Parar'
            break
        else:
            print('Opção invalida: Digite [S] para REPEDIR ou [N] para PARAR')
