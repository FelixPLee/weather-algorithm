
#array que guarda valores de temperaturas máximas
#tempMeses =[None] * 12
tempMeses = [34.3, 36, 31, 31.7, 31, 20, 17, 42.5, 37,  32.1, 33, 23]
while True:
    #define variáveis no escopo "global" (dentro da execução do laço) com valores que retornam erros caso não sejam fornecido valores
    mes = ''
    temp = ''
    menu = ''
    # definindo flags de execução de alterações
    mesVerificado = False
    tempVerificado = False
    menuVerificado = False
    
    #Array de strings de meses do ano por extenso 
    mesesPorExtenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    #array criado filtrando números 'float' sem valor decimal e os convertendo em inteiros por propósitos estéticos
    tempMesesVisual = [int(x) if x == int(x) else x for x in tempMeses]

    #Função que pede ao usuário um valor numérico baseado em um pedido definido no segundo argumento da função.
    #Além de verificar se o o valor é realmente um numero e esta dentro de determinado "Range".
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

    mensagemMenu = '''Digite o número da opção desejada:
1 - Mostrar dados do clima
2 - Editar dado
3 - sair\n'''

    menu = leituraDeValor(menu, mensagemMenu, 3, 1, menuVerificado, True)

    
    if menu == 2:
        #Mensagem que vai Apresentada ao usuário pedindo o valor numérico do mês
        mensagemMes = "Digite o número do mês desejado: "
        #recebe valor de mês e verifica se o numero de mês é valido
        mes = leituraDeValor(mes, mensagemMes, 12, 1, mesVerificado, True )

        # Recebe o valor de temperatura verifica se o numero de temperatura é valido
        mensagemTemp = "Digite o valor da temperatura máxima do mês: "
        temp = leituraDeValor(temp, mensagemTemp, 50, -60, tempVerificado, False)

        #guarda o valor recebido no array 'tempMeses'
        tempMeses[mes -1] = temp
        print('A temperatura máxima no mes de {} foi alterada para {}°C \n'.format(mesesPorExtenso[mes - 1], temp))

    if menu == 1:
        #tabela de dados coletados
        cabecalho = f"| {'Mês':<10} | {'Temperatura Máxima':<18} |"
        linha_separadora = "+" + "-" * 12 + "+" + "-" * 20 + "+"
        soma = 0
        mesesEscald = 0
        maisEscald = -61
        menosEscal = 51
        indexQuente = -1
        indexFrio = -1

        print(linha_separadora)
        print(cabecalho) 
        print(linha_separadora)
        #loop de todos os valores de temperatura máxima com seu respectivo mes atrelado
        for index, temperatura in enumerate(tempMesesVisual) :
            linha = f'| {mesesPorExtenso[index]:<10} | {str(temperatura):^18} |'
            print(linha)
            #soma todos os valores de temperatura para o calculo de média
            soma += temperatura
            if temperatura > 33: mesesEscald += 1
            if temperatura > maisEscald: 
                maisEscald = temperatura 
                indexQuente = index
            if temperatura < menosEscal:
                menosEscal = temperatura
                indexFrio = index


        print(linha_separadora)

        print('Temperatura média máxima anual: ', soma/12, '\n')
        print('Quantidade de meses escaldantes: ' , mesesEscald, '\n')
        print('Mês mais escaldante do ano: ', mesesPorExtenso[indexQuente], '\n')
        print('Mês menos quente do ano: ', mesesPorExtenso[indexFrio], '\n')

        
    if menu == 3: break

        