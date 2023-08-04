def convierte_hexadecimal_a_decimal(numero_hexadecimal: str):
    """
    Función que permite convertir de base hexadecimal a base decimal
    :param numero_hexadecimal: Número en base hexadecimal representado como una cadena
    :return: resultado_decimal: Número en base decimal como entero
    """
    resultado_decimal = 0
    potencia = 0

    for digito in numero_hexadecimal[::-1]:
        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - ord('A') + 10

        resultado_decimal += valor * (16 ** potencia)
        potencia += 1

    return resultado_decimal


def main():
    num = input("Escribe un numero en base hexadecimal: ")
    resultado = convierte_hexadecimal_a_decimal(num)
    print("Convertir: " + num + " al sistema decimal es: " + str(resultado))


if __name__ == '__main__':
    main()