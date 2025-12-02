import sys

from cfgcalculadora import uteis
from cfgcalculadora import operacoes

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
        print("Encerrando programa...")
        print("PROGRAMA ENCERRADO.")
        sys.exit(0)
    
    else:
        print("OPÇÃO INVÁLIDA! POR FAVOR, SELECIONE UMA OPÇÃO VÁLIDA.\n")