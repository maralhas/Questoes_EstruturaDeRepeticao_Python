numero = int(input('Digite um número: '))
tentativas = 0
if numero == 1 or numero == 2:
    tentativas += 1
    print(f'{numero} é primo')
    print(f'Foram executadas {tentativas} para descobrir:')
 
elif numero % 2 == 0:

    print(f'{numero} não é primo!')
    print(f'Foram executadas uma divisão para descobrir isso.')

else:
    tentativas += 1
    primo = True
    for i in range(3, numero, 2):
        tentativas += 1
        if numero % i == 0:
            primo = False
            break
    
    if primo:
        print(f'O número {numero} é primo!')
        print(f'Foram executadas {tentativas} divisões para descobri.')
    
    else:
        print(f'O número {numero} não é primo!')
        print(f'Foram executadas {tentativas} divisões para descobri.')
    
