def convierte_octal_a_decimal(numero_octal: str):
    """
    Función que permite convertir de base octal a base decimal
    :param numero_octal: Número en base octal representado como una cadena
    :return: resultado_decimal: Número en base decimal como entero
    """
    resultado_decimal = 0
    potencia = 0

    for digito in numero_octal[::-1]:
        valor = int(digito)
        resultado_decimal += valor * (8 ** potencia)
        potencia += 1

    return resultado_decimal


def main():
    num = input("Escribe un numero en base octal: ")
    resultado = convierte_octal_a_decimal(num)
    print("Convertir: " + num + " al sistema decimal es: " + str(resultado))


if __name__ == '__main__':
    main()