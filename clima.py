# recebe valor referente a mês e 
while True:
    #define variáveis no escopo global com valores que retornam erros caso não sejam fornecido valores
    mes = ''
    temp = ''
    mesVerificado = False
    tempVerificado = False

    #Array de strings de meses do ano por extenso 
    mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    tempMeses = [None] * 12
    
    
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
                tempMeses[mes] = temp
            else: 
                print('Valor invalido tente novamente\n')
        except ValueError:
            print('Valor invalido tente novamente\n')



        