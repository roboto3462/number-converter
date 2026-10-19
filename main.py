import random, os
historial = []
aciertos = []
ejerciciosRespondidos = []

def resultados(eleccion1, eleccion2, str_original,numDecimal, numeroConvertido, historial):
    print("==================================")
    print("RESULTADO")
    print("==================================")
    print("Número ingresado: " + str_original)
    print("Base de origen: " + eleccion1.capitalize())
    print("Base de destino: " + eleccion2.capitalize())
    print("Resultado: " + numeroConvertido)
    print(" ")
    print("==================================")
    print("PROCEDIMIENTO PASO A PASO")
    print("==================================")

    etapa = 1
    # Solo hay dos etapas, en las que la base de origen y destino es decimal
    terminar_pasos = 0
    base = eleccion1
    destino = eleccion2

    if base != "DECIMAL":
        print(f"ETAPA: {etapa} {base} A DECIMAL")
        for i, char in enumerate(reversed(str_original)):
            match eleccion1:
                case "BINARIO": print(f"{char} X 2^{i} = {str(int(char)*(2**int(i)))}")
                case "OCTAL": print(f"{char} X 8^{i} = {str(int(char)*(8**int(i)))}")
                case "HEXADECIMAL":
                    valor_hex_dec = ""
                    match char:
                        case "A" | "a": valor_hex_dec = "10"
                        case "B" | "b": valor_hex_dec = "11"
                        case "C" | "c": valor_hex_dec = "12"
                        case "D" | "d": valor_hex_dec = "13"
                        case "E" | "e": valor_hex_dec = "14"
                        case "F" | "f": valor_hex_dec = "15"
                        case _: valor_hex_dec = str(char)
                    print(f"{char} (valor {str(valor_hex_dec)}) X 16^{i} = {str(int(valor_hex_dec)*(16**int(i)))}")           
        print(f"Suma de los aportes: {str(numDecimal)}")
        etapa = etapa + 1
    print("")
    
    if destino != "DECIMAL":
        print(f"ETAPA: {etapa} DECIMAL A {destino}")
        cociente = int(numDecimal)
        while True:
            if cociente == 0:
                break
            else:
                match destino:
                    case "BINARIO":
                        print(f"{cociente} / 2: cociente = {cociente // 2}, residuo = {cociente % 2}, dígito = {cociente % 2}")
                        cociente = cociente // 2
                    case "OCTAL":                 
                        print(f"{cociente} / 8: cociente = {cociente // 8}, residuo = {cociente % 8}, dígito = {cociente % 8}")
                        cociente = cociente // 8
                    case "HEXADECIMAL":
                        digito = str(int(cociente) % 16)
                        match digito:
                            case "10": digito = "A"
                            case "11": digito = "B"
                            case "12": digito = "C"
                            case "13": digito = "D"
                            case "14": digito = "E"
                            case "15": digito = "F"
                        print(f"{cociente} / 16: cociente = {cociente // 16}, residuo = {cociente % 16}, dígito = {digito}")
                        cociente = cociente // 16
        print(f"Leer los residuos del último al primero: {numeroConvertido}")
    print("")
    print(f"Resultado final en {destino.capitalize()}: {numeroConvertido}")
    print("")
    print("Conversión agregada al historial.")
    print("")
    input("Presione Enter para continuar...")
    historial.append(f"Entrada: {str(str_original)} Origen: {base} Destino: {destino} Resultado: {numeroConvertido}")
    limpiar()

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

def aDecimal(num, eleccion1):
    val_original = num
    decimal_val = 0
    if not eleccion1 == "DECIMAL":
        # Convertir binario, octal o hexadecimal a decimal por metodo de notacion posicional
        # Invierte el string
        i = len(num) - 1
        inverso_str = ""
        while i >= 0:
            inverso_str += num[i]
            i -= 1
        potencia = 0
        inverso = list(inverso_str)

        # Si toca hexadecimal, remplaza las letras por numeros de 10 al 16 
        valores = {
        "A": 10, "B": 11, "C": 12,
        "D": 13, "E": 14, "F": 15
        }
        for i in range(len(inverso)):
            item = inverso[i].upper()
            if item in valores:
                inverso[i] = valores[item]
        
        # Algoritmo de notacion posicional
        match eleccion1:
            case "BINARIO": multi = 2
            case "OCTAL": multi = 8
            case "HEXADECIMAL": multi = 16
        for digito in inverso:
            decimal_val += int(digito) * (multi ** potencia)
            potencia += 1
    else: decimal_val = int(num)

    return decimal_val

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def tenerNum(eleccion1, eleccion2, historial):
    saltar = 0 
    limpiar()
    while True:
        print("==================================================")
        print("CONVERSIÓN: " + eleccion1 + " A " + eleccion2)
        print("==================================================")
        print("Ingrese un entero no negativo de hasta 128 dígitos.")
        print("Escriba 'volver' para regresar al menú principal.")
        numInput = input("Número a convertir: ")
        # Revisa si tiene errores y si quiere volver
        if numInput == "volver" :
            saltar = 1
            limpiar()
            break
        elif len(numInput) > 128:
            limpiar()
            print("El número a convertir tiene más de 128 dígitos, intente de nuevo.")
        elif set(numInput).issubset({'', ' '}):
            limpiar()
            print("No debe estar vacío o con espacios, intente de nuevo.")            
        else:
            # Revisa si tiene numeros y letras permitidas
            match eleccion1:
                case "BINARIO":
                    if not set(numInput).issubset({'0', '1'}):
                        limpiar()
                        print("Solo 0 y 1 están permitidos, intente de nuevo.")
                    else: break
                case "OCTAL":
                    if not set(numInput).issubset({'0', '1', '2','3','4','5','6','7'}):
                        limpiar()
                        print("Solo números del 0 al 7 están permitidos, intente de nuevo.")
                    else: break
                case "DECIMAL":
                    if not set(numInput).issubset({'0', '1', '2','3','4','5','6','7','8','9'}):
                        limpiar()
                        print("Solo números del 0 al 9 están permitidos, intente de nuevo.")
                    else: break
                case "HEXADECIMAL":
                    if not set(numInput).issubset({'0', '1', '2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F'}):
                        limpiar()
                        print("Solo números y letras entre el 0-9, letras A-F y a-f están permitidos, intente de nuevo.")
                    else: break
    if not saltar == 1:
        str_original = numInput
        numDecimal = str(aDecimal(numInput, eleccion1))
        if not eleccion2 == "DECIMAL":
            numeroConvertido = convEleccion2(numDecimal, eleccion2)
            numeroConvertido = str("".join(reversed(numeroConvertido)))
        else: numeroConvertido = numDecimal
        
        resultados(eleccion1, eleccion2, str_original, numDecimal, numeroConvertido, historial)

def realizarConversion():
    volver = 0 
    saltar = 0
    while True:
        if saltar == 1: break
        print("==================================================")
        print("SELECCIONE LA BASE DEL ORIGEN")
        print("==================================================")
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("0. Volver al menú principal")
        op1 = input("Seleccione una opción: ")
        match op1:
            case "1" | "2" | "3" | "4":
                match op1:
                        case "1":
                            eleccion1 = "BINARIO"
                        case "2":
                            eleccion1 = "OCTAL"
                        case "3":
                            eleccion1 = "DECIMAL"
                        case "4":
                            eleccion1 = "HEXADECIMAL"
                while True:
                    print("==================================================")
                    print("SELECCIONE LA BASE DE DESTINO")
                    print("==================================================")
                    match op1:
                        case "1":
                            print("1. Octal")
                            print("2. Decimal")
                            print("3. Hexadecimal")
                        case "2":
                            print("1. Binario")
                            print("2. Decimal")
                            print("3. Hexadecimal")
                        case "3":
                            print("1. Binario")
                            print("2. Octal")
                            print("3. Hexadecimal")
                        case "4":
                            print("1. Binario")
                            print("2. Octal")
                            print("3. Decimal")
                    print("0. Volver al menú principal")
                    op2 = input("Seleccione una opción: ")
                    match op2:
                        case "1" | "2" | "3":
                            saltar = 1
                            match op1:
                                case "1":
                                    match op2:
                                        case "1" : eleccion2 = "OCTAL"
                                        case "2" : eleccion2 = "DECIMAL"
                                        case "3" : eleccion2 = "HEXADECIMAL"
                                    break
                                case "2":
                                    match op2:
                                        case "1" : eleccion2 = "BINARIO"
                                        case "2" : eleccion2 = "DECIMAL"
                                        case "3" : eleccion2 = "HEXADECIMAL"
                                    break
                                case "3":
                                    match op2:
                                        case "1" : eleccion2 = "BINARIO"
                                        case "2" : eleccion2 = "OCTAL"
                                        case "3" : eleccion2 = "HEXADECIMAL"
                                    break
                                case "4":
                                    match op2:
                                        case "1" : eleccion2 = "BINARIO"
                                        case "2" : eleccion2 = "OCTAL"
                                        case "3" : eleccion2 = "DECIMAL"
                                    break
                        case "0":
                            saltar = 1
                            volver = 1
                            break
                        case _:
                            limpiar()
                            print("Seleccione de nuevo un número de las opciones mostradas.")               
            case "0":
                saltar = 1
                volver = 1
                limpiar()
                break
            case _:
                limpiar()
                print("Seleccione de nuevo un número de las opciones mostradas.")
    if volver == 0:
        tenerNum(eleccion1, eleccion2, historial)
    
def mostrarHistorial():
    while True:
        print("==================================================")
        print("HISTORIAL DE CONVERSIONES")
        print("==================================================")
        if len(historial) == 0:
            print("No hay registros.")
            input("Presione ENTER para continuar...")
            limpiar()
            break
        else: 
            for i, registro in enumerate(historial):
                print(f"Registro {i+1}")
                print(registro)
                print("")
            print(f"Total de registros: {i+1}")
            print("")
            
            print("1. Eliminar un registro")
            print("2. Vaciar historial")
            print("3. Volver al menú principal")
            op = input("Seleccione una opción: ")
            match op:
                case "1":
                    while True:
                        op_del = input("Escriba el número de registro a borrar (0 si cancelar): ")
                        while not op_del.isnumeric():
                            print("Escriba el número que aparece en las opciones.")
                            op_del = input("Escriba el número de registro a borrar (0 si cancelar): ")
                        op_del = int(op_del)
                        if op_del > 0 and op_del <= len(historial):
                            del historial[op_del-1]
                            limpiar()
                            break
                        elif op_del == 0:
                            limpiar()
                            break
                        else:
                            print("Escriba dentro del rango del número de registros.")

                case "2":
                    while True:
                        op = input("¿Está seguro? (1 = Si / 0 = No) ")
                        match op:
                            case "0":
                                limpiar()
                                break
                            case "1":
                                historial.clear()
                                limpiar()
                                break
                            case _:
                                print("Escriba 1 para sí o 0 para no.")
                        
                case "3": 
                    limpiar()
                    break
                case "4":
                    print(len(historial))
                case _:
                    limpiar()
                    print("Seleccione de nuevo un número de las opciones mostradas.")


def modoPractica(aciertos,ejerciciosRespondidos):
    # Hace el calculo antes del porcentaje de aciertos para evitar division por cero
    while True:
        if aciertos.count(1) == 0 and ejerciciosRespondidos.count(1) == 0:
            porcentajeAciertos = 0
        else:
            porcentajeAciertos = ((aciertos.count(1)/ejerciciosRespondidos.count(1))*100)

        print("==================================================")
        print("MODO DE PRÁCTICA")
        print("==================================================")
        print("")
        print("Aciertos: "+ str(aciertos.count(1)))
        print(f"Ejercicios respondidos: {str(ejerciciosRespondidos.count(1))}")
        print(f"Porcentaje de aciertos: {str("%.2f" % (porcentajeAciertos))}%")
        print("")
        print("1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        op = input("Seleccione una opción: ")
        match op:
            case "1":
                limpiar()
                # Ejercicio practica
                bases=["BINARIO","DECIMAL","OCTAL","HEXADECIMAL"]
                base_num=bases[random.randint(0,3)]
                destino_num=bases[random.randint(0,3)]
                while destino_num == base_num:
                    destino_num=bases[random.randint(0,3)]
                
                num_random_decimal = random.randint(0,255)

                if not base_num == "DECIMAL":
                    num_random_base = str("".join(reversed(convEleccion2(str(num_random_decimal),base_num))))
                else: num_random_base = str(num_random_decimal)
                if not destino_num == "DECIMAL":
                    num_random_destino = str("".join(reversed(convEleccion2(str(num_random_decimal),destino_num))))
                else: num_random_destino = str(num_random_decimal)
                
                limpiar() 
                while True:
                    print("==================================================")
                    print("EJERCICIO DE PRÁCTICA")
                    print("==================================================")
                    print(f"Convierta {num_random_base} de {base_num.capitalize()} a {destino_num.capitalize()}.")
                    print("")
                    print("Ingrese únicamente el número de la respuesta.")
                    respuesta = input("Su respuesta: ")
                    match destino_num:
                        case "BINARIO":
                            if not set(respuesta).issubset({'0', '1'}):
                                limpiar()
                                print("Solo 0 y 1 están permitidos, intente de nuevo.")
                            else: 
                                if respuesta == "":
                                    limpiar()
                                    print("No deje la respuesta vacía, intente de nuevo.")
                                else:  
                                    break
                        case "OCTAL":
                            if not set(respuesta).issubset({'0', '1', '2','3','4','5','6','7'}):
                                limpiar()
                                print("Solo números del 0 al 7 están permitidos, intente de nuevo.")
                            else: 
                                if respuesta == "":
                                    limpiar()
                                    print("No deje la respuesta vacía, intente de nuevo.")
                                else:  
                                    break
                        case "DECIMAL":
                            if not set(respuesta).issubset({'0', '1', '2','3','4','5','6','7','8','9'}):
                                limpiar()
                                print("Solo números del 0 al 9 están permitidos, intente de nuevo.")
                            else: 
                                if respuesta == "":
                                    limpiar()
                                    print("No deje la respuesta vacía, intente de nuevo.")
                                else:  
                                    break
                        case "HEXADECIMAL":
                            if not set(respuesta).issubset({'0', '1', '2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F'}):
                                limpiar()
                                print("Solo números y letras entre el 0-9, letras A-F y a-f están permitidos, intente de nuevo.")
                            else: 
                                if respuesta == "":
                                    limpiar()
                                    print("No deje la respuesta vacía, intente de nuevo.")
                                else:  
                                    break
                
                if destino_num == "BINARIO":
                    while respuesta[0] == "0":
                        respuesta = respuesta[1:] 
                
                if respuesta.upper() == num_random_destino:
                    print("Respuesta correcta!")
                    aciertos.insert(0,1)
                else: print(f"Respuesta incorrecta! Era {num_random_destino}.")
                print("")
                ejerciciosRespondidos.insert(0,1)
                print(f"Aciertos: {str(aciertos.count(1))}")
                print(f"Ejercicios respondidos: {str(ejerciciosRespondidos.count(1))}")
                print(f"Porcentaje de aciertos: {str("%.2f" % ((aciertos.count(1)/ejerciciosRespondidos.count(1))*100))}%")
                print("")
                input("Presione enter para continuar...")
                limpiar()
            case "2":
                 while True:
                        op = input("¿Está seguro? (1 = Si / 0 = No) ")
                        match op:
                            case "0":
                                limpiar()
                                break
                            case "1":
                                aciertos.clear()
                                ejerciciosRespondidos.clear()
                                limpiar()
                                break
                            case _:
                                print("Escriba 1 para sí o 0 para no.")
            case "3":
                limpiar()
                break 
            case _:
                limpiar()
                print("Seleccione de nuevo un número de las opciones mostradas.")


while True:
    print("==================================================")
    print("CONVERSOR DE SISTEMAS NUMÉRICOS")
    print("==================================================")
    print("1. Realizar una conversión")
    print("2. Consultar el historial")
    print("3. Iniciar el modo de práctica")
    print("4. Salir")
    op = input("Seleccione una opción: ")
    match op:
        case "1":
            #print("op1")
            limpiar()
            realizarConversion()
        case "2":
            #print("op2")
            limpiar()
            mostrarHistorial()
        case "3":
            #print("op3")
            limpiar()
            modoPractica(aciertos,ejerciciosRespondidos)
        case "4":
            print("Hasta pronto!")
            break 
        case _:
            limpiar()
            print("Seleccione de nuevo un número de las opciones mostradas.")

