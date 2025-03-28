#inicializa uma lista onde sera guardada todos os dados do csv no qual cada item da lista será uma linha com seus dados atribuídos a valores de uma lista
linhasCsv = []
def aberturaDeArquivo(arq):
    with open(arq, 'r') as csvClima:
        # laço for que itera em cada linha do arquivo
        for linha in csvClima:
            #separação
            valores = linha.split(',')
            futuraLinha = []
            try:
                datas = valores[0].split('/')
                #converte valores de data em int
                intDatas = [int(x) for x in datas]
                futuraLinha.append(intDatas)
                for i in range (1, 6):
                    futuraLinha.append(float(valores[i]))
                futuraLinha.append(float(valores[7].replace('\n', '')))
                linhasCsv.append(futuraLinha)
            except:
                #atribui os valores de titulos aos valores da pirmeira linha por isso não tem conversão para float
                for i in range (0, 6): futuraLinha.append(valores[i])
                futuraLinha.append(valores[7].replace('\n', ''))
                linhasCsv.append(futuraLinha)
    #le arquivo indicado pelo usuário
    #aberturaDeArquivo(input('Digite o nome do arquivo csv: '))
aberturaDeArquivo('testedata.csv')
print(linhasCsv[15765])
#registra valor de primeira e ultima data registrada no arquivo
ultimoAno = int(linhasCsv[-1][0][2])
ultimoMes = int(linhasCsv[-1][0][1])
PrimeiroAno = int(linhasCsv[1][0][2])
PrimeiroMes = int(linhasCsv[1][0][1])

mediaporMes = []
dicGrafico = {}
mes = ''
while True:
    #definindo e reinicializando flags
    menuVerificado = False
    #definindo e reinicializando variveis
    menu = ''

####################FUNÇÃO QUE LE ARQUIVO####################

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

####################FUNÇÃO DE EXECUÇÃO DE EVENTOS####################

    #função utilizada na solução do evento 1
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

    #Função utilizada na solução do evento 2    
    def porMes(intervaloTempo, valor):
        somaDoMes = 0
        viraMes = 0
        maiorValor = -999
        dataMaiorValor = ''
        for i in range(intervaloTempo[0], intervaloTempo[1]):
            mesAtual = linhasCsv[i][0][1]
            if viraMes != mesAtual:
                viraMes = mesAtual
                if somaDoMes > maiorValor:
                    maiorValor = somaDoMes
                    dataMaiorValor = linhasCsv[i-1][0]
                #zera o valor da soma para passar para o proximo mex
                somaDoMes = 0
            somaDoMes += linhasCsv[i][valor]
        return {'SomaDeMaiorValor': maiorValor, 'Data': dataMaiorValor}
    
    #Função utilizada na solução do evento 3 e 4 
    def mediaPorMesUnico(inic, final, valor):
        meses  = {}
        mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        somaMensal = 0
        contadorValores = 0
        anoAtual = 0
        mesAtual = 0
        #define flags de validação dos dados fornecidos
        dataVerificada = False
        inicMesVerificado = False
        #mensagens apresentadas para receber valores iniciais e finais de dada
        inicMesMen = 'Digite o valor numérico referente ao mes da análise: '
        while dataVerificada == False:
            inicMes = ''
            inicMes = leituraDeValor(inicMes, inicMesMen, 12, 1, inicMesVerificado, True)
            dataVerificada = True
        for index in range(inic, final):
            diaAtual = linhasCsv[index][0][0]
            if linhasCsv[index][0][1] == inicMes:
                somaMensal += linhasCsv[index][valor]
                contadorValores = contadorValores + 1
            if diaAtual == 1 and mesAtual == 1:
                if index -1 != inic:
                    mesAtual = 13
            if (mesAtual != inicMes) and ([diaAtual ,mesAtual, anoAtual] == [1, inicMes +1, anoAtual]):
                media = round(somaMensal/contadorValores)
                chave = f'{mesesPorExtenso[inicMes -1]} {anoAtual}'
                meses.update({chave : media})
                somaMensal = 0
                contadorValores = 0
            mesAtual = linhasCsv[index][0][1]
            anoAtual = linhasCsv[index][0][2]
        return [meses, mesesPorExtenso[inicMes -1]]

####################CRIAÇÃO DE TABELAS####################

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

####################EXECUÇÃO DE EVENTOS####################

    menuMen = '''Digite o valor da opção que deseja acessar:
1 - Visualização de intervalo de dados.
2 - Mês mais chuvoso.
3 - Média da temperatura mínima de um determinado mês.
4 - Gráfico de barras  com as médias de temperatura mínima de um determinado mês nos últimos 11 anos.
5 - Média geral da temperatura mínima do mes determinado no gráfico.
6 - sair\n'''

    menu = leituraDeValor(menu, menuMen, 6, 1, menuVerificado, True)
    visualTipo = ''
    if menu == 1:
        visualTipoVerificador = False

        tempoAnalisado = intervaloDeData()
        print(tempoAnalisado[0])
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
    
    if menu == 2:
        chuvao = porMes([1, len(linhasCsv)], 1) 
        dadoTitulo = ' Precipitação (mm)   |'
        separador = '+' + '-' * 12 + '+' + '-' *21 + '+'
        maiorPrecipitacao = chuvao['SomaDeMaiorValor']
        dataMaiorPrecipitacao = chuvao['Data']
        dado =  f'{str(maiorPrecipitacao):^20} |'
        cabecalho = f'|    Data    |' + dadoTitulo
        linha = f'| {dataMaiorPrecipitacao[0]:02d}/{dataMaiorPrecipitacao[1]:02d}/{dataMaiorPrecipitacao[2]} |' + dado
        print(separador)
        print(cabecalho)
        print(separador)
        print(separador)
        print(linha)
        print(separador)

    if menu == 3:
        print('Serão considerados validos dados de janeiro de 2006 até Junho de 2016!')
        mediaporMes = mediaPorMesUnico(16437, len(linhasCsv), 3)
        dicMeses = mediaporMes[0]
        cabecalho = '|      Data      |  Média de temperatura mínima (°C)  |'
        separador = '+' + '-' * 16 + '+' + '-' *35 + '+'
        print(separador)
        print(cabecalho)
        print(separador)
        for data, valor in dicMeses.items():
            linha = f'|{data:^16}|{valor:^35}|'
            print(linha)
            print(separador)
             
    mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if menu == 4:
        #importa biblioteca usada para graficos
        import matplotlib.pyplot as plt
        print('Serão considerados validos dados de janeiro de 2006 até Junho de 2016!')
        mediaporMes = mediaPorMesUnico(16437, len(linhasCsv), 3)
        dicGrafico = mediaporMes[0]
        mes = mediaporMes[1]
        meses = dicGrafico.keys()
        valores = dicGrafico.values()

        plt.bar(meses,valores, width = 0.7)
        plt.xticks(rotation=45)  #Rotaciona o label em 45 graus
        plt.tight_layout() #Ajusta o espaçamento
        plt.xlabel(f'Meses de {mes} ao longo')
        plt.ylabel('Temperatura em °C')
        plt.title(f'Médias de temperatura mínima de {mes}')
        plt.show(block=False)
        input("Press Enter to close the figure...")
        plt.close()

    if menu == 5:
        if dicGrafico == {}:
            print('É preciso definir um mes na opção de grafico para acessar essa funcionalidade \n')
        else:
            somaTotal =0
            contador = 0
            for temp in dicGrafico.values():
                somaTotal += temp
                contador += 1
            mediaGeral = somaTotal/contador
            if mesesPorExtenso.index(mes) > 6: anoFinal = 2015
            else: anoFinal = 2016
            frase = f' A média geral de temperatura mínima dos meses de {mes} de 2006 até {anoFinal} foi de: {mediaGeral}°C'
            print(frase)
    

    if menu == 6: break