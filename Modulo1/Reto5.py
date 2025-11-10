def main():
    print("-"*20)

    try:
        alumnos=int(input("Hola! ingresa la cantidad de alumnos inscritos: "))
        lista1=[]
        for i in range(0, alumnos):
            x=input("\nIngresa el nombre y calificacion del alumno: ")
            lista0=x.split(", ")
            lista1.extend(lista0)
    except ValueError:
        print("Ingresa un número entero")
    try:
        extrusornon=list(range(1,alumnos*2,2))
        extrusorpar=list(range(0,alumnos*2,2))
        
        try:
            calif=[float(lista1[a]) for a in extrusornon]
            for calificacion in calif:
                if calificacion < 0 or calificacion > 10:
                    print(f"Error: La calificación {calificacion} no está entre 0 y 10")
                    return
        except ValueError:
            print("La calificacion debe ser numerica")
            return
        names=[lista1[b] for b in extrusorpar]
        
        reprobados=[]
        aprobados=[]
        excelentes=[]
        
        for z in range(len(names)):
            nombre=names[z]
            calificacion=calif[z]
            if calificacion < 6:
                reprobados.append((nombre, calificacion))
            elif calificacion >= 6 and calificacion < 10:
                aprobados.append((nombre, calificacion))
            elif calificacion == 10:
                excelentes.append((nombre, calificacion))

# stats generales:
        promedio=sum(calif)/len(calif)
        minimo=min(calif)
        maximo=max(calif)

#? impresiones generales
        print("-"*20)
        print(f"Cantidad de alumnos: {alumnos}")
        print(f"Promedio Grupal: {promedio}")
        print(f"Calificacion más baja: {minimo}")
        print(f"Calificacion más alta: {maximo}")

#! impresiones de listas
        print(f"\n-ALUMNOS EXCELENTES (10)-")
        if excelentes:
            for nombre, calif in excelentes:
                print(f"  {nombre}: {calif}")
        else:
            print("No hay alumnos con calificación excelente")
    
        print(f"\n-ALUMNOS APROBADOS (6-9)-")
        if aprobados:
            for nombre, calif in aprobados:
                print(f"  {nombre}: {calif}")
        else:
            print("  No hay alumnos aprobados")
    
        print(f"\n-ALUMNOS REPROBADOS (<6)-")
        if reprobados:
            for nombre, calif in reprobados:
                print(f"  {nombre}: {calif}")
        else:
            print("  No hay alumnos reprobados")


    except UnboundLocalError:
        print("-"*20)
    except IndexError:
        print("La lista debe estar separada por una coma y un espacio")
    
main()
