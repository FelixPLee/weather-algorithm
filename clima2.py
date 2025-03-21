while True:
    menuVerificado = False
    linhasCsv = []


    def aberturaDeArquivo(arq):
        with open(arq, 'r') as csvClima:
            for linha in csvClima:
                valores = linha.split(',')
                futuraTupla = []
                try:
                    futuraTupla.append(valores[0])
                    for i in range (1, 6):
                        futuraTupla.append(float(valores[i]))
                    futuraTupla.append(float(valores[7].replace('\n', '')))
                    linhasCsv.append(tuple(futuraTupla))
                except:
                    for i in range (0, 6): futuraTupla.append(valores[i])
                    futuraTupla.append(valores[7].replace('\n', ''))
                    linhasCsv.append(tuple(futuraTupla))

                
            
    #aberturaDeArquivo(input('Digite o nome do arquivo csv: '))
    aberturaDeArquivo('testedata.csv')
    
    print(linhasCsv[0])
    print(linhasCsv[1])
    input('123')

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