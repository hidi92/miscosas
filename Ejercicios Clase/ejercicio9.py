import os
def limpiar():
    os.system("cls")
def ejer9():
    listanombres= ["a"]
    listatelefonos= ["a"]
    contador =int(0)
    ciclo1 = True

    while ciclo1 == True:
        ciclo2 = True

        while ciclo2 == True:
            ciclo2 = False
            nombres = input("Introduce un nombre")
            telefonos = input("Introduce un telefono")
            for e in range (0,contador+1):
                if telefonos == listatelefonos[e]:
                    print("Numero repetido, vuelve a intentarlo")
                    limpiar()
                    ciclo2 = True

        listanombres.append(nombres)
        listatelefonos.append(telefonos)
        contador = contador + 1
        salir= input("Escribe 'n' para mostrar agenda | Escribe 's' para añadir otro contacto")
        if salir == "s":
            limpiar()
            continue
        elif salir=="n":
            limpiar()
            for i in range (1,contador+1):
                print("Nombre: ",listanombres[i])
                print("Telefono: ",listatelefonos[i])
            ciclo1 = False
        else:
            limpiar()
            print("Has introducido una opcion incorrecta, adios")
            break
ejer9()