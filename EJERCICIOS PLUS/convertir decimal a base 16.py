def convierte_hexadecimal(numero: int):
    """
    Función que permite convertir a hexadecimal recibiendo un número entero decimal
    :param numero:
    :return: conversion
    """
    conversion = ''
    resultado = numero
    while int(resultado) != 0:
        residuo = int(resultado) % 16
        resultado = int(resultado) // 16

        # Convertir el residuo en dígito hexadecimal
        if residuo < 10:
            conversion = str(residuo) + conversion
        else:
            conversion = chr(ord('A') + (residuo - 10)) + conversion
    return conversion


def main():
    num = input("Escribe un numero entero de base decimal: ")
    numero = int(num)
    resultado = convierte_hexadecimal(numero)
    print("Convertir: " + str(numero) + " al sistema hexadecimal es: " + resultado)


if __name__ == '__main__':
    main()
