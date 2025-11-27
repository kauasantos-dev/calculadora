def validar_int(numero):
    try:
        numero = int(numero)
        return numero
    except ValueError:
        raise ValueError("O número não deve conter letras, espaços ou caracteres especiais.")

def validar_float(numero):
    try:
        numero = float(numero)
        return numero
    except ValueError:
        raise ValueError("O número não deve conter letras, espaços ou caracteres especiais.")