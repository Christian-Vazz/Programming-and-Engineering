contador = 0
lista = []

while contador <= 3:
    adicionar = input('Deseja adicionar algo na lista? [s]im [n]ão: ').lower().startswith('n')
    
    if adicionar:
        print('Obrigado por usar o listened')
        print(lista)
        break
    
    crud = input('Digite o que deseja adicionar: ')
    lista.append(crud)
    print(lista)
    
    contador += 1
    
    if contador == 3:
        for index in range(contador):
            print(index, lista[index])
    