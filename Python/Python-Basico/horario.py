user_hour = input('Digite o horário: ')
try:
    user_hour = int(user_hour)
    if (user_hour >= 0) and (user_hour <= 11):
        print('Bom dia')
    elif (user_hour >= 12) and (user_hour <= 17):
        print('Boa tarde')
    elif (user_hour >= 18) and (user_hour <= 23):
        print('Boa noite')
    else:
        print('Horário inválido')
except:
    print(f'"{user_hour}" não é um horário')