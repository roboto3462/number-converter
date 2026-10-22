import random, os, historialC, practica, convEleccion2, realizarConversion
historial = []
aciertos = []
ejerciciosRespondidos = []

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
            limpiar()
            realizarConversion.realizarConversion(historial, limpiar, convEleccion2)
        case "2":
            limpiar()
            historialC.mostrarHistorial(historial,limpiar)
        case "3":
            limpiar()
            practica.modoPractica(aciertos, ejerciciosRespondidos, historial, limpiar, random, convEleccion2)
        case "4":
            print("Hasta pronto!")
            break 
        case _:
            limpiar()
            print("Seleccione de nuevo un número de las opciones mostradas.")

