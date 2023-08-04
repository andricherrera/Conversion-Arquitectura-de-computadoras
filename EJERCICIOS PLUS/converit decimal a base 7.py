def convierte_base_siete(numero: int):
    """
    Función que permite convertir a base 7 recibiendo un número entero decimal
    :param numero:
    :return: conversion
    """
    conversion = ''
    resultado = numero
    while int(resultado) != 0:
        residuo = int(resultado) % 7
        resultado = int(resultado) // 7
        conversion = str(residuo) + conversion
    return conversion


def main():
    num = input("Escribe un numero entero de base decimal: ")
    numero = int(num)
    resultado = convierte_base_siete(numero)
    print("Convertir: " + str(numero) + " al sistema base 7 es: " + resultado)


if __name__ == '__main__':
    main()
