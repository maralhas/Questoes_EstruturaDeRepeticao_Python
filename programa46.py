
saltos = []
melhor = pior = media = 0

while True:
    entrada = input('Digite o nome do atleta: ')
    nome = entrada
    if entrada == '':
        break
    else:
        print(f'Atreta: {nome}')
        print ('')

        primeiro_salto = float(input('Primeiro Salto: '))
        saltos.append(primeiro_salto)
        segundo_salto = float(input('Segundo Salto: '))
        saltos.append(segundo_salto)
        terceiro_salto = float(input('terceiro Salto: '))
        saltos.append(terceiro_salto)
        quarto_salto = float(input('Quarto Salto: '))
        saltos.append(quarto_salto)
        quinto_salto = float(input('quinto Salto: '))
        saltos.append(quinto_salto)
        print('')
       
        melhor = max(saltos)
        pior = min(saltos)
        media = (sum(saltos)-melhor - pior) / 3
        
        print(f'Melhor salto:  {melhor} m')
        print(f'Pior salto: {pior} m')
        print('Média dos demais saltos: {:.2f}'.format(media) + ' m')
        print ('')
        print('Resultado final:')
        print(nome + ' {:.2f}'.format(media) + ' m')

        entrada = ''