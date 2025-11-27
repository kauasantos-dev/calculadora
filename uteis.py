def adicionar(dicionario):
    try:
        historico = arquivo_r()
        if not historico:
            historico = []
            historico.append(dicionario)
            arquivo_w(historico)
        else:
            historico.append(dicionario)
            arquivo_w(historico)
    except FileNotFoundError:
        historico = []
        historico.append(dicionario)
        arquivo_w(historico)