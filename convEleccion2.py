def convEleccion2(numDecimal, eleccion2):
    match eleccion2:
            case "BINARIO": division = 2
            case "OCTAL": division = 8
            case "HEXADECIMAL": division = 16

    cociente = int(numDecimal)
    numConvertido = []

    while True:
        if cociente == 0:
            break
        else:
            numConvertido.append(str(int(cociente) % division))
            cociente = int(cociente) // division

    # Si toca hexadecimal, remplaza las letras por numeros de 10 al 16 
    if eleccion2 == "HEXADECIMAL":
        valores = {
        "10": "A", "11": "B", "12": "C",
        "13": "D", "14": "E", "15": "F"
        }
        for i in range(len(numConvertido)):
            item = numConvertido[i]
            if item in valores:
                numConvertido[i] = valores[item]

    numConvertido = list(numConvertido)
    return numConvertido