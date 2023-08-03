def convierte_binario(numero: int):
    """
    Función que permite convertir a binario recibiendo un número entero decimal
    :param numero:
    :return: conversion
    """
    conversion = ''
    resultado = numero
    while int(resultado) != 0:
        print(str(int(resultado)) + ' ÷ 2 = ' + str(int(resultado / 2)) + ' Su residuo es: ' + str(int(resultado % 2)))
        residuo = int(resultado) % 2
        resultado = int(resultado) / 2
        conversion = conversion + str(residuo)
    return conversion


def invierte_conversion(conversion: str):
    """
    Función que permite invertir el resultado de conversión y se pueda mostrar adecuadamente
    :param conversion:
    :return: invertir_conversión
    """
    invertir_conversion = ''
    for caracter in conversion:
        invertir_conversion = caracter + invertir_conversion
    return invertir_conversion


def main():
    num = input("Escribe un numero entero de base decimal: ")
    numero = int(num)
    conver = convierte_binario(numero)
    resultado = invierte_conversion(conver)
    print("Convertir: " + str(numero) + " al sistema binario es: " + resultado)


if __name__ == '__main__':
    main()