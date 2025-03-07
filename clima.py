# recebe valor referente a mês e 
while True:
    mes = int(input("Digite o número do mês desejado: "))
    #check para ver se o numero de mês é valido
    if (mes < 1) or (mes > 12):
        print('invalid number')
    else: 
        break
