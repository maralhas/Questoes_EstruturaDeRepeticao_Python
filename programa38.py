from datetime import date

salario_atualizando = salario_inicial = 1000
almento = 0.015
data_atual = date.today()
ano = data_atual.year
print(ano)

for ano_inicial in range(1997, ano +1):
    salario_atualizando = salario_atualizando + (salario_inicial * almento)
    print(f'Porcentagem em {ano_inicial}: {almento}' + ' -- Novo Salario: ' '{:.2f}'.format(salario_atualizando))
    almento = almento * 2
