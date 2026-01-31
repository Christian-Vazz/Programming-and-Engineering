print('=' * 30)
print('\033[34mINFORMAÇÕES DE USUÁRIO\033[0m')
print('=' * 30)

nome_usuario = input('Digite seu nome: ').lower() or 'sem nome'
idade_usuario = input('Digite sua idade: ').lower() or 'sem idade'

if (nome_usuario != 'sem nome') and (idade_usuario != 'sem idade'):
    qtd_espacos = nome_usuario.count(' ')
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    print(f'Seu nome tem {qtd_espacos}' if qtd_espacos > 0 else 'Seu nome não tem espaços')
    print(f'Seu nome tem {len(nome_usuario)}')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[len(nome_usuario) - 1]}')
else:
    print('Desculpe, você deixou campos vazios')
