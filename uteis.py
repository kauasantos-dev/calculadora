import gerenciar_arquivos
import validadores

def adicionar(dicionario):
    try:
        historico = gerenciar_arquivos.arquivo_r()
        if not historico:
            historico = []
            historico.append(dicionario)
            gerenciar_arquivos.arquivo_w(historico)
        else:
            historico.append(dicionario)
            gerenciar_arquivos.arquivo_w(historico)
    except FileNotFoundError:
        historico = []
        historico.append(dicionario)
        gerenciar_arquivos.arquivo_w(historico)

def menu_opcoes():
    print("Selecione uma opção abaixo (digite o número da opção):")
    print("\n[1]- Soma\n[2]- Subtração\n[3]- Divisão\n[4]- Multiplicação\n[5]- Histórico de operações\n[6]- Apagar histórico\n[7]- Sair\n")

def solicitar_numeros():
    lista_numeros = []
    while True:
        numero = input("Informe dois números ou mais (digite 'sair' para finalizar): ")
        if numero.lower() == 'sair':
            break
        numero = validadores.validar_numero(numero)
        lista_numeros.append(numero)
    
    if len(lista_numeros) < 2:
        raise ValueError("Quantidade de números insuficientes para realizar a operação.\n")
    
    return lista_numeros