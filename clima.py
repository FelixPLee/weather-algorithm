
#array que guarda valores de temperaturas máximas
#tempMeses =[None] * 12
tempMeses = [34.3, 36, 31, 31.7, 31, 20, 17, 42.5, 37,  32.1, 33, 23]
while True:
    #define variáveis no escopo "global" (dentro da execução do laço) com valores que retornam erros caso não sejam fornecido valores
    mes = ''
    temp = ''
    # definindo flags de execução de alterações
    mesVerificado = False
    tempVerificado = False
    #array criado filtrando números 'float' sem valor decimal e os convertendo em inteiros por propósitos estéticos
    tempMesesVisual = [int(x) if x == int(x) else x for x in tempMeses]



    #Array de strings de meses do ano por extenso 
    mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    #verifica se o numero de mês é valido
    while not(mesVerificado):
        mes = input("Digite o número do mês desejado: ")
        print('\n')
        #em caso de erro (devido falha na conversão de string para int) o algorítimo executa o bloco de código que segue abaixo do 'except'
        try:
            mes = int(mes)
            if (mes <= 12) and (mes >= 1):
                mesVerificado = True
            else:
                print('Valor invalido tente novamente \n')
        except ValueError:
            print('Valor invalido tente novamente \n')


    # Recebe o valor de temperatura
    while not(tempVerificado):
        temp = input("Digite o valor da temperatura máxima do mês: ")
        print('\n')
        #verifica se o valor de temperatura é um numero
        try:
            temp = float(temp)
            if (temp > -60) and (temp < 50):
                print('A temperatura máxima no mes de {} foi de {}°C'.format(mesesPorExtenso[mes - 1], temp))
                print('\n')
                tempVerificado = True
                #guarda o valor recebido no array 'tempMeses'
                tempMeses[mes -1] = temp
            else: 
                print('Valor invalido tente novamente\n')
        except ValueError:
            print('Valor invalido tente novamente\n')

    #tabela de dados coletados
    cabecalho = f"| {'Mês':<10} | {'Temperatura Máxima':<18} |"
    linha_separadora = "+" + "-" * 12 + "+" + "-" * 20 + "+"

    print(linha_separadora)
    print(cabecalho) 
    print(linha_separadora)
    #loop de todos os valores de temperatura máxima com seu respectivo mes atrelado
    for index, mes in enumerate(mesesPorExtenso) :
        linha = f'| {mes:<10} | {str(tempMesesVisual[index]):^18} |'
        print(linha)
    print(linha_separadora)

        