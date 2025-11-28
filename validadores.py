def validar_numero(numero):
    try:
        if numero.isdigit():
            numero = int(numero)
        else:
            numero = float(numero)
        return numero
    except ValueError:
        raise ValueError("O número não deve conter letras, espaços ou caracteres especiais.")