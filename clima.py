# recebe valor referente a mês e 
while True:
    #define variáveis no escopo global com valores que retornam erros caso não sejam fornecido valores
    mes = 0
    temp = 500

    #Array de strings de meses do ano por extenso 
    mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    mes = int(input("Digite o número do mês desejado: "))
    #check para ver se o numero de mês é valido
    if (mes < 1) or (mes > 12):
        print('invalid number')
        
    # Recebe o valor de temperatura
    temp = int(input("Digite o valor da temperatura máxima em Celsius refente ao mês"))
    if (temp > 50) or (temp < -60):
        print('invalid number')
    else:
        print('A temperatura máxima no mes de {mesesPorExtenso[mes]} foi de {temp}C' )
        