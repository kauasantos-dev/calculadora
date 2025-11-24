def soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def subtracao(lista):
    resultado = lista[0]
    for i in range(1, len(lista)):
        resultado -= lista[i]
    return resultado

def divisao(a, b):
    return a/b

def multiplicacao(lista):
    mult = 1
    for numero in lista:
        mult *= numero
    return mult