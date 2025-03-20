while True:
    menuVerificado = False
    linhasCsv = ''

    def aberturaDeArquivo(arq):
        with open(arq, 'r') as csv:
            climaData = csv.reader(csv)
            for linha in climaData: print(linha)
    #aberturaDeArquivo(input('Digite o nome do arquivo csv: '))

    with open('testedata.csv', 'r') as csvClima:
        try:
            for linha in csvClima: print(linha)
            sucesso = input('suc')
        except:
            erro = input('123')

    input('')
    def leituraDeValor(valor, pedido, max, min, flag, inteiro):
        while not(flag):
            valor = input(pedido)
            print('\n')
            try:
                valor = float(valor)
                if (valor <= max) and (valor >= min):
                    if (inteiro == True) and (valor != int(valor)):
                        print('Valor invalido\n') 
                    elif inteiro == True:
                        return int(valor) 
                    else:
                        flag = True
                        return valor
                else: print('Valor invalido, informe um valor dentro do estabelecido\n')
            except ValueError: print('Valor invalido\n')
    

    menuMen = ''