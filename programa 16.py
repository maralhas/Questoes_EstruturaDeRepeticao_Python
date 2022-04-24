atual = 0
anterior = 1
resultado = 0

while resultado < 500:
    resultado = anterior + atual
    anterior = atual
    atual = resultado 
    print(resultado, end = ' ')