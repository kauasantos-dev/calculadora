import gerenciar_arquivos

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