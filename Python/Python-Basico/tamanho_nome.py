nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Nome curto')
elif (len(nome) >= 5) and (len(nome) <= 6):
    print('Nome normal')
elif len(nome) > 6:
    print('Nome grande')
else:
    print('Erro')