first_value = input('Digite um valor: ')
second_value = input('Digite um valor: ')

if first_value > second_value:
    print(f'{first_value=} é maior que {second_value=}')
elif second_value > first_value:
    print(f'{second_value=} é maior que {first_value=}')
elif first_value == second_value:
    print('Os valores são iguais')
else:
    print('Algo errado!')