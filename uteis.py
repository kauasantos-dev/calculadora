import gerenciar_arquivos
import validadores

def ver_historico():
    historico = gerenciar_arquivos.arquivo_r()
    if not historico:
        print("O HISTÓRICO DE OPERAÇÕES ESTÁ VAZIO.\n")
    else:
        print("HISTÓRICO DE OPERAÇÕES:")
        for produto in historico:
            for chave, valor in produto.items():
                print(f"{chave} = {valor}")

def apagar_historico():
    gerenciar_arquivos.arquivo_w([])

def salvar_historico(nova_operação_efetuada):
    historico_salvo = gerenciar_arquivos.arquivo_r()
    if not historico_salvo:
        historico_salvo = [nova_operação_efetuada]
    else:
        historico_salvo.append(nova_operação_efetuada)
    gerenciar_arquivos.arquivo_w(historico_salvo)

def historico_nova_operacao(lista_numeros, operação, resultado):
    for valor in range(len(lista_numeros)):
        lista_numeros[valor] = str(lista_numeros[valor])

    operacao_realizada = f" {operação} ".join(lista_numeros)

    return {operacao_realizada: resultado}

def menu_opcoes():
    print("\n[1]- Soma\n[2]- Subtração\n[3]- Divisão\n[4]- Multiplicação\n[5]- Ver histórico de operações\n[6]- Apagar histórico\n[7]- Sair\n")

def solicitar_numeros(simbolo_da_operacao):
    lista_numeros = []
    if simbolo_da_operacao == '/':
        dividendo, divisor = validadores.validar_numero(input("Informe o primeiro número: ")), validadores.validar_numero(input("Informe o segundo número: "))
        validadores.validar_divisor(divisor)
        lista_numeros.append(dividendo)
        lista_numeros.append(divisor)
        return lista_numeros
    
    while True:
        numero = input("Informe dois números ou mais (digite uma letra para finalizar): ")
        if numero.isalpha():
            break
        numero = validadores.validar_numero(numero)
        lista_numeros.append(numero)
    
    if len(lista_numeros) < 2:
        raise ValueError("Quantidade de números insuficiente para realizar a operação.\n")
    
    return lista_numeros

def realizar_operacao(operacao_selecionada, simbolo_da_operacao):
    try:
        lista_numeros = solicitar_numeros(simbolo_da_operacao)
    except (ValueError, ZeroDivisionError) as erro:
        print(f"\nERRO: {erro}")
        return False
    resultado = operacao_selecionada(lista_numeros)
    exibir_resultado_operacao(historico_nova_operacao(lista_numeros, simbolo_da_operacao, round(resultado, 2)))
    salvar_historico(historico_nova_operacao(lista_numeros, simbolo_da_operacao, round(resultado, 2)))

def exibir_resultado_operacao(operacao_realizada):
    operacao = list(operacao_realizada.keys())
    resultado = list(operacao_realizada.values())
    print(f"\n{operacao[0]} = {resultado[0]}")