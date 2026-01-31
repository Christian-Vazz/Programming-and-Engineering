from os import system
from time import sleep


lista = []
condition = True
while condition:
    option = input('Selecione uma opção \n[i]nserir [a]pagar [l]istar: ').lower()
    
    if option == 'i':
        system('cls')
        inserir = input('Digite o que deseja inserir: ')
        print(f'Valor inserido "{inserir}"')
        lista.append(inserir)

    elif option == 'a':
        system('cls')
        apagar = input('Digite o indice que deseja apagar: ')

        if apagar.isdigit() and len(lista) >= 0:
            apagar = int(apagar)
            if apagar > len(lista):
                print('Indice inválido...')
            else:
                del lista[apagar]
        else:
            print('Indice inválido...')
        
    elif option == 'l':
        system('cls')
        if bool(lista):
            print('Listando...')
            sleep(1)
            for indice, valor in enumerate(lista):
                print(indice, valor)
                sleep(1)
        else:
            print('Nada para listar...')
    
    else:
        print('Opção inválida')