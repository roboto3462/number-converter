def mostrarHistorial(historial,limpiar):
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