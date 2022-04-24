tabuada = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input("Terminar em: "))

while True:
    if inicio < fim :
        break
    else: 
        print('O falor de inicio deve ser menor que o final ')
        inicio = int(input('Começar por: '))
        fim = int(input("Terminar em: "))

for inicio in range(inicio, fim +1):
    print(f'{tabuada} X {inicio} = {tabuada * inicio}')
