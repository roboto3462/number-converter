def modoPractica(aciertos, ejerciciosRespondidos, historial, limpiar, random, convEleccion2):
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
                # num_random_decimal = 0

                if num_random_decimal != 0 :
                    if not base_num == "DECIMAL":
                        num_random_base = str("".join(reversed(convEleccion2.convEleccion2(str(num_random_decimal),base_num))))
                    else: num_random_base = str(num_random_decimal)
                    if not destino_num == "DECIMAL":
                        num_random_destino = str("".join(reversed(convEleccion2.convEleccion2(str(num_random_decimal),destino_num))))
                    else: num_random_destino = str(num_random_decimal)
                else: 
                    num_random_base = "0" 
                    num_random_destino = "0"
                
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
                
                if len(respuesta) > 1:
                    stop = 0
                    while respuesta[0] == "0" and stop == 0:
                        if len(respuesta) == 1: 
                            stop = 1
                        else: respuesta = respuesta[1:]
                
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