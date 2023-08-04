def convierte_base_nueve_a_decimal(numero_base_nueve: str):
    """
    Función que permite convertir de base nueve a base decimal
    :param numero_base_nueve: Número en base nueve representado como una cadena
    :return: resultado_decimal: Número en base decimal como entero
    """
    resultado_decimal = 0
    potencia = 0

    for digito in numero_base_nueve[::-1]:
        valor = int(digito)
        resultado_decimal += valor * (9 ** potencia)
        potencia += 1

    return resultado_decimal


def main():
    num = input("Escribe un numero en base nueve: ")
    resultado = convierte_base_nueve_a_decimal(num)
    print("Convertir: " + num + " al sistema decimal es: " + str(resultado))


if __name__ == '__main__':
    main()