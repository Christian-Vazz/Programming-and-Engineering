from os import system as sys

letras_acertadas = ''
palavra_secreta = input('Digite uma palavra: ')
contador = 0
sys('cls')
while True:
    letra_jogador = input('Digite uma letra: ')
    quantidade_de_letras = len(letra_jogador)
    contador += 1
    
    if (quantidade_de_letras > 1) or (quantidade_de_letras < 1):
        print('Quantidade de letra inválida!')
        print('Digite novamente!')
        continue
    
    if letra_jogador in palavra_secreta:
        letras_acertadas += letra_jogador
    
    palavra_formada = ''
      
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Parabéns, você ganhou!')
        print('Tentativas', contador)
        escolha = input('Deseja jogar: [s]im ou [n]ão: ').lower()
        if escolha[0] == 'n':
            print('Obrigado por jogar!')
            break
        elif escolha[0] == 's':
            tentativas = 0
            continue
        else:
            print('Opção inválida!')
            continue
    contador+=1
    
    
     
    
    
    