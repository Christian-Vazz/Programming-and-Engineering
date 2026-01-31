name = input('Digite seu nome: ')
size_name = len(name)
contador = 0
new_name = ''
while contador < size_name:
    new_name += '*' + name[contador]
    contador += 1
print(new_name)