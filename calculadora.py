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
        elif opcao == '2':
            resultado = operacoes.subtracao(lista_numeros)

    elif opcao == '3':
        while True:
            try:
                n1, n2 = input("Informe o primeiro número: "), input("Informe o segundo número: ")
                n1 = validar_int(n1) if n1.isdigit() else validar_float(n1)
                n2 = validar_int(n2) if n2.isdigit() else validar_float(n2)
                resultado = divisao(n1, n2)
                resultado = round(resultado, 2) if isinstance(resultado, float) else resultado
                print(f"\n{n1} / {n2} = {resultado}\n")
                dicionario[f"{n1} / {n2}"] = resultado
                adicionar(dicionario)
                break
            except ZeroDivisionError:
                print("\nErro: Divisão por 0 (zero) não é permitida.\n")
                continue
            except ValueError as e:
                print("Erro: ", e, " Tente novamente.\n")
    
    elif opcao == '4':
        while True:
            try:
                numero = input("Informe dois números ou mais (digite 'sair' para finalizar): ")
                if numero.lower() == 'sair':
                    break
                numero = validar_int(numero) if numero.isdigit() else validar_float(numero)
                lista.append(numero)
            except ValueError as e:
                print("Erro: ", e, " Tente novamente.\n")
        if len(lista) < 2:
            print("Erro: Quantidade de números insuficiente para realizar a operação.\n")
        else:
            resultado = multiplicacao(lista)
            resultado = round(resultado, 2) if isinstance(resultado, float) else resultado
            print("\n")
            for i in range(len(lista)):
                if i < len(lista) - 1:
                    variavel += f"{lista[i]} * "
                    print(f"{lista[i]} *", end=" ")
                else:
                    variavel += f"{lista[i]}"
                    print(f"{lista[i]} = {resultado}\n")
            dicionario[variavel] = resultado
            adicionar(dicionario)
    
    elif opcao == '5':
        try:
            historico = arquivo_r()
            if not historico:
                print("\nHistórico vazio.\n")
            else:
                print("Seu histórico de operações:\n")
                for operacao in historico:
                    for chave, valor in operacao.items():
                        print(f"{chave} = {valor}\n")
        except FileNotFoundError:
            print("Histórico vazio.\n")
    
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