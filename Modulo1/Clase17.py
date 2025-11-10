estudiantes={}
materias_validas=("resistencia de los materiales", "control clasico", "programacion avanzada")

def obtener_calificaciones():

    calificaciones = []
    for i in range(3):
        while True:
            try:
                calif = float(input(f"Ingrese calificación {i+1}: "))
                if 0 <= calif <= 10:  
                    calificaciones.append(calif)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10")
            except ValueError:
                print("Error: Debe ingresar un número válido")
    return calificaciones

def registrar_estudiante():
    id_estudiante=input("Ingresa ID del estudiante: ").strip()
    if not id_estudiante:
        print("Error: El id no puede estar vacío")
        return
    if id_estudiante in estudiantes:
        print("Error: Ya existe un estudiante con ese ID")
        return
    
    #! Obtener nombre
    nombre = input("Ingrese nombre del estudiante: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío")
        return
    
    #! Mostrar materias válidas
    print("\nMaterias válidas:")
    for i, materia in enumerate(materias_validas, 1):
        print(f"{i}. {materia}")
    
    # !Obtener materia válida
    while True:
        materia = input("Ingrese la materia: ").strip().lower()
        if materia in materias_validas:
            break
        else:
            print("Error: Materia no válida. Las materias válidas son:")
            for mat in materias_validas:
                print(f"  - {mat}")
    
    # !Obtener calificaciones
    print("\nIngrese 3 calificaciones:")
    calificaciones = obtener_calificaciones()
    
    # !Crear registro del estudiante con diccionarios
    estudiantes[id_estudiante] = {
        "nombre": nombre,
        "materia": materia,
        "calificaciones": calificaciones
    }
    print(f"\nEstudiante {nombre} registrado exitosamente con ID: {id_estudiante}")

def buscar_estudiante():
    id_estudiante=input("Ingrese el ID del estudiante a buscar: ").strip()
    if id_estudiante in estudiantes:
        buscado=estudiantes[id_estudiante]
        print("ID: ",id_estudiante)
        print(f"Nombre: {buscado['nombre']}")
        print(f"Materia: {buscado['materia']}")
        print(f"Calificaciones: {buscado['calificaciones']}")
    else:
        print("Error no se encontro ningun estudiante con ese ID")

def calcular_promedio():
    id_estudiante=input("Ingrese el ID del alumno que desea calcular promedio: ").strip()
    if not id_estudiante:
        print("Error: No puede haber ID vacío")
        return
    if id_estudiante in estudiantes:
        estudiante=estudiantes[id_estudiante]
        calificaciones=estudiante['calificaciones']
        promedio=sum(calificaciones)/len(calificaciones)
        
        print(f"\nPromedio de {estudiante['nombre']}:")
        print(f"Calificaciones: {calificaciones}")
        print(f"Promedio: {promedio}")
        
        # ?Estado del estudiante
        if 10>promedio>=6:
            estado = "Aprobado"
        elif promedio == 10:
            estado = "Excelente"
        else:
            estado = "Reprobado"
        print(f"Estado: {estado}")
    else:
        print("Error: No se encontró ningún estudiante con ese ID")

def ver_todos_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    
    for i, (id_est, datos) in enumerate(estudiantes.items(), 1):
        print(f"{i}. ID: {id_est} | Nombre: {datos['nombre']} | Materia: {datos['materia']}")

def mostrar_cursos_unicos():
    #!En el reto no estaba incluido que tenia que hacer esta opcion asi que lo implemente como un contador de alumnos inscritos en la materia 
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    materias_registradas = set()
    for estudiante in estudiantes.values():
        materias_registradas.add(estudiante['materia'])
    
    print("Materias con estudiantes inscritos:")
    for i, materia in enumerate(sorted(materias_registradas), 1):
        cantidad = sum(1 for est in estudiantes.values() if est['materia'] == materia)
        print(f"{i}. {materia} ({cantidad} estudiantes)")


def main():
    menu_opciones=True
    while menu_opciones:
        print("-"*20)
        print("Menu opciones\n1. Registrar\n2. Buscar\n3. Promedio\n4. Ver todos\n5. Cursos unicos\n6. Salir")
        print("-"*20)
        opciones=input("Ingresa la opción que quieras realizar: ").strip().lower()
        if opciones=="registrar" or opciones=="1":
            registrar_estudiante()
        elif opciones=="buscar" or opciones=="2":
            buscar_estudiante()
        elif opciones=="promedio" or opciones=="3":
            calcular_promedio()
        elif opciones=="ver_todos" or opciones=="4":
            ver_todos_estudiantes()
        elif opciones=="cursos_unicos" or opciones=="5":
            mostrar_cursos_unicos()
        elif opciones=="salir" or opciones=="6":
            print("Espero volver a vernos y gracias por usar mi programa")
            break
        else:
            print("No seleccionaste ninguna opcion, intentalo de nuevo")
main()
#? En este si me tarde como 6 hrs en total pero estuvo divertido, segun yo no tiene ninguna falla 