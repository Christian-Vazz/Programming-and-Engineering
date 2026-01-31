frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. ' 'Python foi criado por Guido Van Rossum.'
    
contador = 0

qtd_letras_frase = len(frase)
letra_apareceu_mais_vezes = ''
qtd_letra_apareceu_mais_vezes = 0

while contador < qtd_letras_frase:
    letra_atual = frase[contador]
    qtd_letra_apareceu_atual = frase.count(frase[contador]) # Conta quantas vezes a letra aparece
    
    if frase[contador] == ' ':
        contador+=1
        continue
    
    if qtd_letra_apareceu_mais_vezes < qtd_letra_apareceu_atual: 
        qtd_letra_apareceu_mais_vezes = qtd_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual
    
    contador+=1
    
print(f'"{letra_apareceu_mais_vezes}"', qtd_letra_apareceu_mais_vezes)