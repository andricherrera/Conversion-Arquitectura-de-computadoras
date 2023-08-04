def convierte_octal(numero: int):
    """
    Función que permite convertir a octal recibiendo un número entero decimal
    :param numero:
    :return: conversion
    """
    conversion = ''
    resultado = numero
    while int(resultado) != 0:
        print(str(int(resultado)) + ' ÷ 8 = ' + str(int(resultado / 8)) + ' Su residuo es: ' + str(int(resultado % 8)))
        residuo = int(resultado) % 8
        resultado = int(resultado) / 8
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
    conver = convierte_octal(numero)
    resultado = invierte_conversion(conver)
    print("Convertir: " + str(numero) + " al sistema octal es: " + resultado)


if __name__ == '__main__':
    main()
