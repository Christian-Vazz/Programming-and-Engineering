condicao = True
operacao_valida = '+-*/'
while condicao:
    valor1 = input('Valor: ')
    operacao = input('Operação: ')
    valor2 = input('Valor: ')
    
    contagem_op = len(operacao)
    numeros_validos = None
    
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        numeros_validos = True
    except:
        numeros_validos = None

    if (operacao not in operacao_valida) or (contagem_op != 1):
        print('Operação inválida ou além do limite de 1x')
        continue
        
    if numeros_validos is None:
        print('Um ou mais valores inválidos!')
        continue
    
    if operacao == '+':
        print(f'{valor1} {operacao} {valor2} = {valor1 + valor2}')
    elif operacao == '-':
        print(f'{valor1} {operacao} {valor2} = {valor1 - valor2}')
    elif operacao == '*':
        print(f'{valor1} {operacao} {valor2} = {valor1 * valor2}')
    elif operacao == '/':
        print(f'{valor1} {operacao} {valor2} = {valor1 / valor2}')
    else:
        print('Algo deu errado nas operações')
    
    sair = input('Deseja [s]air? ').lower().startswith('s')
    if sair:
        print('Obrigado por utilizar a calculadora simples!')
        condicao = False