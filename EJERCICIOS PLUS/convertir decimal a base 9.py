def convierte_base_n(numero: int, base: int):
    """
    Función que permite convertir un número decimal a cualquier base (hasta base 10)
    :param numero: Número entero decimal
    :param base: Base a la que se quiere convertir (hasta base 10)
    :return: conversion
    """
    if base < 2 or base > 10:
        raise ValueError("La base debe estar entre 2 y 10")

    conversion = ''
    resultado = numero

    while int(resultado) != 0:
        print(str(int(resultado)) + f' ÷ {base} = ' + str(int(resultado / base)) + f' Su residuo es: ' + str(int(resultado % base)))
        residuo = int(resultado) % base
        resultado = int(resultado) / base
        conversion = conversion + str(residuo)

    return conversion


def invierte_conversion(conversion: str):
    """
    Función que permite invertir el resultado de conversión y mostrarlo adecuadamente
    :param conversion:
    :return: invertir_conversion
    """
    invertir_conversion = ''
    for caracter in conversion:
        invertir_conversion = caracter + invertir_conversion
    return invertir_conversion


def main():
    num = input("Escribe un número entero de base decimal: ")
    numero = int(num)
    base_n = int(input("Escribe la base a la que quieres convertir (entre 2 y 10): "))
    conver = convierte_base_n(numero, base_n)
    resultado = invierte_conversion(conver)
    print(f"Convertir: {numero} al sistema de base {base_n} es: {resultado}")


if __name__ == '__main__':
    main()
