enesimo = int(input('Infaorme a posição de n: '))
atual = 0
anterior = 1
resultado = 0

for i in range(enesimo):
    resultado = anterior + atual
    anterior = atual
    atual = resultado 
    print(resultado, end = ' ')
    
