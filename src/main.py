def validar_texto(texto):
    if type(texto) is not str:
        raise TypeError("Esse campo deve ser um texto obrigatório.")
    return texto

def validar_decimal(decimal):
    if type(decimal) is not float:
        raise TypeError("Esse campo deve ser número decimal obrigatório.")
    if decimal < 0:
        raise TypeError("Somente números positivos.")
    return decimal


def validar_inteiro(inteiro):
    if type(inteiro) is not int:
        raise TypeError("Esse campo deve ser número inteiro obrigatório.")
    if inteiro < 0:
        raise TypeError("Somente números positivos")
    return inteiro

print(validar_texto("Olá"))