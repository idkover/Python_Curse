
    #! Holaa te paso el reto 4 que te mostre el Lunes 20/10/2025 corregido 
def main():
    opciones=int(0)
    Lista_0=["leche", "pan", "manzanas"]
    while opciones!=4:
        print("-"*20)
        print("Menu opciones\n1. Añadir\n2. Quitar\n3. Revisar\n4. Salir")
        try:
            opciones=int(input("Selecciona una opcion: "))
            print("-"*20)
            if opciones==1:
                No_Void=input("Ingresa el articulo que quieras agregar: ").strip().lower()
                if not No_Void:
                    print("Favor de no ingresar campos vacíos")
                    continue
                Lista_0.append(No_Void)
                print(f"Lista actual: {Lista_0}")
            elif opciones==2:
                try:    
                    Lista_0.remove(input("Ingresa el dato que quieras remover: ").lower().strip())
                except ValueError:
                    print("Este articulo no está en la lista")
                print(f"Lista actual: {Lista_0}")
            elif opciones==3:
                print(f"Tu lista actual es: {Lista_0}")
                ordenar=input("Deseas ordenarla alfabeticamente?\ny/n\n")
                ordenar=ordenar.lower().strip()
                if ordenar=="y":
                    Lista_0.sort()
                    print(f"Ordenada: {Lista_0}")
                elif ordenar=="n":
                    print("Ok")
                    print("-"*20)
                else:
                    print("Opcion no valida")
            elif opciones==4: 
                print("Nos volveremos a ver...")
                break
            else: print("No seleccionaste ninguna opcion, intenta de nuevo")
        except ValueError:
            print("Ingresa un numero entero por favor")
    #! Primera vez q uso try except, grande w3schools 

main()