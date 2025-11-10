
#def main_continua():
#    for num in range(10):
#        if num % 2==0:
#            continue #!salta a la siguiente iteracion 
#        print(num)

def reto6():   
    menu_opciones=True
    Inventario=["agua","comida"]
    while menu_opciones:
        print("-"*20)
        print("Menu opciones\n1. añadir\n2. quitar\n3. ver\n4. inspeccionar\n5. salir")
        print("-"*20)


        opciones=input("Ingresa la opción que quieras realizar: ")
        opciones=opciones.lower().strip()

        #! Opcion añadir
        if opciones == "añadir" or opciones=="1":
            Inv_Temporal=input("Ingresa el articulo que quieras agregar: ")
            Inv_Temporal=Inv_Temporal.strip().lower()
            if not Inv_Temporal:
                print("Favor de no ingresar campos vacíos")
                continue
            Inventario.append(Inv_Temporal)
            print(f"Articulo agregado: {Inventario}")

        #! Opcion quitar
        elif opciones == "quitar" or opciones=="2":
            if not Inventario:
                print("-"*20)
                print("Lista vacía")
                continue
            else:
                try:
                    Inv_Temporal=input("Ingresa el dato que quieras remover: ")
                    Inv_Temporal=Inv_Temporal.strip().lower()
                    Inventario.remove(Inv_Temporal)
                except ValueError:
                    print("Este articulo no está en la lista")
                print(f"Lista actual: {Inventario}")

            #! Opcion ver
        elif opciones=="ver" or opciones=="3":
            if not Inventario:
                print("-"*20)
                print("Lista vacía")
                continue
            else:
                print(f"Tu lista actual es: {Inventario}")
                Ordenar=input("Deseas ordenarla alfabeticamente?\ny/n\n")
                Ordenar=Ordenar.lower().strip()
                if Ordenar=="y":
                    Inventario.sort()
                    print(f"Ordenada: {Inventario}")
                elif Ordenar=="n":
                    print("Ok")
                    print("-"*20)
                else:
                    print("Opcion no valida")

        #! Opcion Inspeccionar
        elif opciones=="inspeccionar" or opciones=="4":
            if not Inventario:
                print("-"*20)
                print("Lista vacía")
                continue
            else:
                try:
                    Posicion=int(input("Ingresa la posicion del item a inspeccionar: "))-1
                    if Posicion<0:
                        print("Esta posicion no se encuentra en la lista")
                        continue
                    else:
                        Dato_Posicion=Inventario[Posicion]
                        print(f"El dato en la posicion {Posicion} es: '{Dato_Posicion}'")
                except ValueError:
                    print("Ingresa un valor numérico, ej: '5'")
                except IndexError:
                    print("Esta posicion no se encuentra en la lista")

        #! Opcion Salir 
        elif opciones=="salir" or opciones=="5":
            print("Nos veremos de nuevo")
            break
        else:
            print("No seleccionaste ninguna opcion, intentalo de nuevo")



reto6()