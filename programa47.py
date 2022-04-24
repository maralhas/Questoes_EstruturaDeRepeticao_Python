notas = []

nome_ginasta = input('Digite o nome do(a) ginasta: ')

for i in range(7):
    notas.append(float(input('Nota: ')))

pior = min(notas)
melhor = max(notas)
media = (sum(notas) - pior - melhor) / 5

print(f'''Resultado final:
Atleta: {nome_ginasta}
Melhor nota: {melhor}
Pior nota: {pior}
Média: {media}''')
