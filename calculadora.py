import sys

import uteis
import operacoes

print("\n===== MENU DE OPÇÕES =====")
while True:
    uteis.menu_opcoes()
    opcao = input("SELECIONE UMA OPÇÃO ACIMA (digite o número da opção): ")

    if opcao == '1':
        uteis.realizar_operacao(operacoes.soma, '+')

    elif opcao == '2':
        uteis.realizar_operacao(operacoes.subtracao, '-')

    elif opcao == '3':
        uteis.realizar_operacao(operacoes.divisao, '/')

    elif opcao == '4':
        uteis.realizar_operacao(operacoes.multiplicacao, '*')
    
    elif opcao == '5':
        uteis.ver_historico()

    elif opcao == '6':
        uteis.apagar_historico()

    elif opcao == '7':
        print("Programa encerrado.\n")
        sys.exit(0)
    
    else:
        print("Opção inválida. Por favor, selecione uma das opções abaixo.\n")