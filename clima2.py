#inicializa uma lista onde sera guardada todos os dados do csv no qual cada item da lista será uma linha com seus dados atribuidos a valores de uma tupla
linhasCsv = []
def aberturaDeArquivo(arq):
    with open(arq, 'r') as csvClima:
        # laço for que itera em cada linha do arquivo
        for linha in csvClima:
            #separação
            valores = linha.split(',')
            futuraTupla = []
            try:
                #atribui valores da linha a lista que futuramente se trona a tupla inserida na lista  de linhas
                datas = valores[0].split('/')
                #converte valores de data em int
                intDatas = [int(x) for x in datas]
                futuraTupla.append(intDatas)
                for i in range (1, 6):
                    futuraTupla.append(float(valores[i]))
                futuraTupla.append(float(valores[7].replace('\n', '')))
                # lista é adicionada como tupla `q lista de tuplas de dados`
                linhasCsv.append(futuraTupla)
            except:
                #atribui os valores de titulos aos valores da pirmeira linha por isso não tem conversão para float
                for i in range (0, 6): futuraTupla.append(valores[i])
                futuraTupla.append(valores[7].replace('\n', ''))
                linhasCsv.append(futuraTupla)
    #le arquivo indicado pelo usuário
    #aberturaDeArquivo(input('Digite o nome do arquivo csv: '))
aberturaDeArquivo('testedata.csv')
print(linhasCsv[15765])
#registra valor de primeira e ultima data registrada no arquivo
ultimoAno = int(linhasCsv[-1][0][2])
ultimoMes = int(linhasCsv[-1][0][1])
PrimeiroAno = int(linhasCsv[1][0][2])
PrimeiroMes = int(linhasCsv[1][0][1])

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
        #define flags de validação dos dados fornecidos
        dataVerificada = False
        inicAnoVerificado = False
        inicMesVerificado = False
        finalAnoVerificado = False 
        finalMesVerificado = False
        #mensagens apresentadas para receber valores iniciais e finais de dada
        inicAnoMen = 'Digite o valor nuérico referente ao ano inicial da análise: '
        inicMesMen = 'Digite o valor nuérico referente ao mes inicial da análise: '
        finalAnoMen = 'Digite o valor nuérico referente ao ano final da análise: '
        finalMesMen = 'Digite o valor nuérico referente ao mes final da análise: '
        while dataVerificada == False:
            inicAno = ''
            inicMes = ''
            finalAno =''
            finalMes =''
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
                inicIndex = 0
                finalIndex = 0
                anosBissexto = [1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
                for index, linha in enumerate(linhasCsv):
                    if [1, inicMes, inicAno] in linha:
                        inicIndex = index
                    if [1, finalMes, finalAno] in linha:
                        if (finalMes== 2) and (finalAno in anosBissexto):
                            finalIndex = index + 28
                        elif finalMes == 2:
                            finalIndex = index + 27
                        elif finalMes in [4,6,9,11]:
                            finalIndex = index + 29
                        else:
                            finalIndex = index + 30
                    if (inicIndex > 0) and (finalIndex > 0):
                        dataVerificada = True
                        return [inicIndex, finalIndex]
                    
    def intervaloDeMes():
        #define flags de validação dos dados fornecidos
        dataVerificada = False
        inicAnoVerificado = False
        inicMesVerificado = False
        #mensagens apresentadas para receber valores iniciais e finais de dada
        print('Serão considerados validos dados de janeiro de 2006 até Junho de 2016!')
        inicAnoMen = 'Digite o valor nuérico referente ao ano inicial da análise: '
        inicMesMen = 'Digite o valor nuérico referente ao mes inicial da análise: '
        while dataVerificada == False:
            inicAno = ''
            inicMes = ''
            inicAno = leituraDeValor(inicAno, inicAnoMen, 2016, 2006, inicAnoVerificado, True)
            inicMes = leituraDeValor(inicMes, inicMesMen, 12, 1, inicMesVerificado, True)
            if (inicAno > ultimoAno) or ((inicAno == ultimoAno) and (inicMes > ultimoMes)):
                print("Dado não registrado no arquivo")
            else:
                inicIndex = 0
                finalIndex = 0
                anosBissexto = [1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
                for index, linha in enumerate(linhasCsv):
                    if [1, inicMes, inicAno] in linha:
                        inicIndex = index
                        if (inicMes== 2) and (inicAno in anosBissexto):
                            finalIndex = index + 28
                        elif inicMes == 2:
                            finalIndex = index + 27
                        elif inicMes in [4,6,9,11]:
                            finalIndex = index + 29
                        else:
                            finalIndex = index + 30
                    if (inicIndex > 0) and (finalIndex > 0):
                        dataVerificada = True
                        return [inicIndex, finalIndex]



    def tabelaCompleta(inic, final):

        cabecalho = '|    Data    | Precipitação (mm)   | Temperatura Máxima (°C)  | Temperatura Mínima (°C) | Umidade Relativa (%) | Velocidade do Vento (m/s) |'
        separador = '+' + '-' * 12 + '+' + '-' * 21 + '+' + '-' * 26 + '+' + '-' * 25 + '+' + '-' * 22 + '+' + '-' * 27 + '+'
        print(separador)
        print(cabecalho)
        for index in range(inic, final, 1):
            dadosAtual = linhasCsv[index]
            data = dadosAtual[0]
            linha = f"| {data[0]:02d}/{data[1]:02d}/{data[2]} | {str(dadosAtual[1]):^19} | {str(dadosAtual[2]):^24} | {str(dadosAtual[3]):^23} | {str(dadosAtual[4]):^20} | {str(dadosAtual[5]):^25} |"
            print(separador)
            print(linha)
        print(separador)

    def tabelaIndividual(inic, final, identificador):
        for index in range(inic, final, 1):
            dadosAtual = linhasCsv[index]
            separador = ''
            if identificador == 2: 
                dadoTitulo = ' Precipitação (mm)   |'
                separador = '+' + '-' * 12 + '+' + '-' *21 + '+'
                dado =  f'{str(dadosAtual[identificador -1]):^21} |'
            elif identificador == 3: 
                dadoTitulo = ' Temperatura Máxima (°C)  | Temperatura Mínima (°C) |'
                separador = '+' + '-' * 12 + '+' + '-' * 26 + '+' + '-' * 25 + '+'
                dado =  f'{str(dadosAtual[identificador -1]):^24} | {str(dadosAtual[identificador]):^25} |'
            else:
                dadoTitulo = ' Velocidade do Vento (m/s) |'
                separador = '+' + '-' * 12 + '+' +  '-' * 27 + '+'
                dado =  f'{str(dadosAtual[identificador +1]):^27} |'
            print(separador)
            print(cabecalho)
            cabecalho = f'|    Data    |' + dadoTitulo
            data = dadosAtual[0]
            linha = f'| {data[0]:02d}/{data[1]:02d}/{data[2]} |' + dado
            print(separador)
            print(linha)
        print(separador)



    menuMen = '''Digite o valor da opção que deseja acessar:
1 - Visualização de intervalo de dados
2 - Mês mais chuvoso
3 - Média da temperatura mínima de um determinado mês
4 - Gráfico de barras
5 - Média geral da temperatura mínima de um determinado mês
6 - sair\n'''

    menu = leituraDeValor(menu, menuMen, 5, 1, menuVerificado, True)
    visualTipo = ''
    if menu == 1:
        visualTipoVerificador = False

        tempoAnalisado = intervaloDeData()
        visualTipoMen = '''Digite o valor da opção que deseja acessar:
1 - todos os dados
2 - apenas os de precipitação
3 - apenas os de temperatura
4 - apenas os de umidade e vento\n'''

        visualTipo = leituraDeValor(visualTipo, visualTipoMen, 4, 1, visualTipoVerificador, True)
        if visualTipo == 1:
            tabelaCompleta(tempoAnalisado[0], tempoAnalisado[1])
        else:
            tabelaIndividual(tempoAnalisado[0], tempoAnalisado[1], visualTipo)

    if menu == 4:
        #importa biblioteca usada para graficos
        import matplotlib.pyplot as plt
        tempoAnalisado = intervaloDeMes()
        
        categories = ['A', 'B', 'C', 'D']
        values = [15, 20, 12, 25]
        plt.bar(categories, values, color=['blue', 'green', 'red', 'cyan'])
        plt.title('Bar Chart Example')
        #plt.show()

    if menu == 6: break