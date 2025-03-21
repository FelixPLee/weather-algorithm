#inicializa uma lista onde sera guardada todos os dados do csv no qual cada item da lista será uma linha com seus dados atribuidos a valores de uma tupla
linhasCsv = []
def aberturaDeArquivo(arq):
    with open(arq, 'r') as csvClima:
        # laço for que itera em cada linha do arquivo
        print('oi')
        for linha in csvClima:
            #separação
            valores = linha.split(',')
            futuraTupla = []
            try:
                #atribui valores da linha a lista que futuramente se trona a tupla inserida na lista  de linhas
                futuraTupla.append(tuple(valores[0].split('/')))
                for i in range (1, 6):
                    futuraTupla.append(float(valores[i]))
                futuraTupla.append(float(valores[7].replace('\n', '')))
                # lista é adicionada como tupla `q lista de tuplas de dados`
                linhasCsv.append(tuple(futuraTupla))
            except:
                #atribui os valores de titulos aos valores da pirmeira linha por isso não tem conversão para float
                for i in range (0, 6): futuraTupla.append(valores[i])
                futuraTupla.append(valores[7].replace('\n', ''))
                linhasCsv.append(tuple(futuraTupla))
    #le arquivo indicado pelo usuário
    #aberturaDeArquivo(input('Digite o nome do arquivo csv: '))
aberturaDeArquivo('testedata.csv')

print(linhasCsv[1])

while True:
    #definindo e reinicializando flags
    menuVerificado = False
    #definindo e reinicializando variveis
    menu = ''

    def leituraDeValor(valor, pedido, max, min, flag, inteiro):
        #Enquanto a falg não for desativada o algoritmo segue pedindo um valor válido até que o mesmo seja retornado pelo usuário
        while not(flag):
            valor = input(pedido)
            print('\n')
            #em caso de erro (devido falha na conversão de string para int) o algorítimo executa o bloco de código que segue abaixo do 'except'
            try:
                valor = float(valor)
                #Confere se o valor fornecido está estabelecido no "Range" da função
                if (valor <= max) and (valor >= min):
                    #Caso o argumento "inteiro" seja definido como "True" verifica se o valor é um número inteiro
                    if (inteiro == True) and (valor != int(valor)):
                        print('Valor invalido\n') 
                    elif inteiro == True:
                        return int(valor) 
                    else:
                        flag = True
                        return valor
                #Mensagens de erro caso o valor seja maior ou menor que o solicitado ou não seja um numero
                else: print('Valor invalido, informe um valor dentro do estabelecido\n')
            except ValueError: print('Valor invalido\n')

    def intervaloDeData():
        #registra valor de primeira e ultima data registrada no arquivo
        ultimoAno = int(linhasCsv[-1][2])
        ultimoMes = int(linhasCsv[-1][1])
        PrimeiroAno = int(linhasCsv[1][2])
        PrimeiroMes = int(linhasCsv[1][1])
        #define flags de validação dos dados fornecidos
        dataVerificada = False
        inicAnoVerificado = False
        inicMesVerificado = False
        finalAnoVerificado = False 
        finalMesVerificado = False
        #mensagens apresentadas para receber valores iniciais e finais de dada
        inicAnoMen = 'Digite o valor nuérico referente ao ano inical da análise: '
        inicMesMen = 'Digite o valor nuérico referente ao mes inical da análise: '
        finalAnoMen = 'Digite o valor nuérico referente ao ano final da análise: '
        finalMesMen = 'Digite o valor nuérico referente ao mes final da análise: '

        while dataVerificada == False:
            inicAno = leituraDeValor(inicAno, inicAnoMen, 2016, 1961, inicAnoVerificado, True)
            inicMes = leituraDeValor(inicMes, inicMesMen, 12, 1, inicMesVerificado, True)
            finalAno = leituraDeValor(finalAno, finalAnoMen, 2016, 1961, finalAnoVerificado, True)
            finalMes = leituraDeValor(finalMes, finalMesMen, 12, 1, finalMesVerificado, True)
        
            if finalAno < inicAno:
                print("Valores Fornecidos não congruentes")
            elif (finalAno == inicAno) and (inicMes > finalMes):
                print("Valores Fornecidos não congruentes")
            elif (finalAno > ultimoAno) or ((finalAno == ultimoAno) and (finalMes > ultimoMes)):
                print("Dado não registrado no arquivo")
            elif (inicAno < PrimeiroAno) or ((inicAno == PrimeiroAno) and (inicMes < PrimeiroMes)):
                print("Dado não registrado no arquivo")
            else:
                return [inicAno, inicMes, finalAno, finalMes]
                dataVerificada =True
            

                
            

    menuMen = '''Digite o valor da opção que deseja acessar:
1 - Visualização de intervalo de dados
2 - Mês mais chuvoso
3 - Média da temperatura mínima de um determinado mês
4 - Gráfico de barras
5 - Média geral da temperatura mínima de um determinado mês\n'''

    menu = leituraDeValor(menu, menuMen, 5, 1, menuVerificado, True)

    if menu == 1:
        visualTipoMen = '''Digite o valor da opção que deseja acessar:
1 - todos os dados
2 - apenas os de precipitação
3 - apenas os de temperatura
4 - apenas os de umidade e vento'''