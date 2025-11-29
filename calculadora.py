import sys

import uteis
import operacoes

print("\n===== MENU DE OPÇÕES =====\n")
while True:
    uteis.menu_opcoes()
    opcao = input()

    if opcao == '1' or opcao == '2':
        try:
            lista_numeros = uteis.solicitar_numeros()
        except ValueError as e:
            print("Erro: ", e)
            continue
        if opcao == '1':
            resultado = operacoes.soma(lista_numeros)
            operacao_realizada = uteis.historico_nova_operacao(lista_numeros, '+', resultado)
            uteis.exibir_operacao(operacao_realizada)
        elif opcao == '2':
            resultado = operacoes.subtracao(lista_numeros)
            operacao_realizada = uteis.historico_nova_operacao(lista_numeros, '-', resultado)
            uteis.exibir_operacao(operacao_realizada)

    elif opcao == '3':
        try:
            lista_numeros = uteis.solicitar_numeros('3')
        except ValueError as erro:
            print(f"ERRO: {erro}")
            continue
        resultado = operacoes.divisao(lista_numeros)
        operacao_realizada = uteis.historico_nova_operacao(lista_numeros, '/', resultado)
        uteis.exibir_operacao(operacao_realizada)
        uteis.salvar_historico(operacao_realizada)

    elif opcao == '4':
        try:
            lista_numeros = uteis.solicitar_numeros()
        except ValueError as erro:
            print(f"ERRO: {erro}")
            continue
        resultado = operacoes.multiplicacao(lista_numeros)
        operacao_realizada = uteis.historico_nova_operacao(lista_numeros, '*', resultado)
        uteis.exibir_operacao(operacao_realizada)
        uteis.salvar_historico(operacao_realizada)
    
    elif opcao == '5':
        uteis.ver_historico()

    elif opcao == '6':
        try:
            historico = arquivo_r()
            if not historico:
                print("Histórico vazio.\n")
            else:
                historico = []
                arquivo_w(historico)
                print("Histórico apagado com sucesso!\n")
        except FileNotFoundError:
            print("Histórico vazio.\n")

    elif opcao == '7':
        print("Programa encerrado.\n")
        sys.exit(0)
    
    else:
        print("Opção inválida. Por favor, selecione uma das opções abaixo.\n")