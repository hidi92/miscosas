import os, time
def limpiar():
    time.sleep(2)
    os.system("cls")
def menu():
    salir = False
    while salir == False:

        print ("""Escribe una opcion para seleccionar ejercicio
               0.Salir
               1.Ejercicio numero mayor
               2.Ejercicio contar caracteres
               3.Ejercicio contar vocales
               4.Ejercicio sumar y multiplicar
               5.Ejercicio Numeros palindromos""")
        menuopc = input("Introduce una opcion")

        if menuopc == "0":
            print("Adios")
            salir = True
            continue
        if menuopc == "1":
            print ("Has seleccionado el Ejercicio 1, empezemos:")
            import ejercicio1
            limpiar()
            continue
        if menuopc == "2":
            print ("Has seleccionado el Ejercicio 2, empezemos:")
            import ejercicio2
            limpiar()
            continue
        if menuopc == "3":
            print ("Has seleccionado el Ejercicio 3, empezemos:")
            import ejercicio3
            limpiar()
            continue
        if menuopc == "4":
            print ("Has seleccionado el Ejercicio 4, empezemos:")
            import ejercicio4
            limpiar()
            continue
        if menuopc == "5":
            print ("Has seleccionado el Ejercicio 5, empezemos:")
            import ejercicio5
            limpiar()
            continue
        else:
            print("Error: Has introducido una opcion no valida")
            limpiar()
menu()