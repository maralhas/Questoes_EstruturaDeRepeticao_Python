
login = password = ''

while login == password:
    login = input('Informe o nome de usuário: ')
    password = input('Informe a senha: ')
    if login == password :
        print('ERRO!!! - Nome de usuário e senha não podem ser iguais. ')