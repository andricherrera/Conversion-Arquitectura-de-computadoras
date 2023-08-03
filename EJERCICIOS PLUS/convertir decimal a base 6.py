def convierte_base_seis(numero: int):
    """
    Función que permite convertir a base 6 recibiendo un número entero decimal
    :param numero:
    :return: conversion
    """
    conversion = ''
    resultado = numero
    while int(resultado) != 0:
        residuo = int(resultado) % 6
        resultado = int(resultado) // 6
        conversion = str(residuo) + conversion
    return conversion


def main():
    num = input("Escribe un numero entero de base decimal: ")
    numero = int(num)
    resultado = convierte_base_seis(numero)
    print("Convertir: " + str(numero) + " al sistema base 6 es: " + resultado)


if __name__ == '__main__':
    main()
