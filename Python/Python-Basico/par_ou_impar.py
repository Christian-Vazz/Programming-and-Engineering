numero_usuario = input('Digite um número: ')

try:
    numero_usuario = int(numero_usuario)

    if numero_usuario % 2 == 0:
        print(f'O número {numero_usuario} é par')
    else:
        print(f'O número {numero_usuario} é impar')
except:
    print(f'"{numero_usuario}" não pode ser convertido para inteiro')