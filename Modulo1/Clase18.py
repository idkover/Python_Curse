# Funcion lambda
# duplicar_lambda= lambda x:x*2
# print(duplicar_lambda(5))


base_de_partes = {}
COMPONENTES_VALIDOS = ("Motor", "Sensor", "Batería", "Chasis")

def obtener_float_valido(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0.0 <= valor <= 100.0:
                return valor
            else:
                print("Error: El valor debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, introduce un número.")


def obtener_tipo_valido():
    while True:
        print(f"Tipos disponibles: {', '.join(COMPONENTES_VALIDOS)}")
        tipo = input("Introduce el tipo de componente: ").strip().capitalize()
        if tipo in COMPONENTES_VALIDOS:
            return tipo
        else:
            print(f"Error: '{tipo}' no es un tipo de componente válido.")


def registrar_parte(base_datos):
    print("\nRegistro de Nueva Pieza")
    
    #TODO Pedir Número de Serie y verificar que no exista ya
    while True:
        num_serie = input("Introduce el Número de Serie (S/N): ").strip().upper()
        if not num_serie:
            print("Error: El Número de Serie no puede estar vacío.")
        elif num_serie in base_datos:
            print(f"Error: El S/N '{num_serie}' ya existe en la base de datos.")
        else:
            break

    tipo_componente = obtener_tipo_valido()
    
    resultados_pruebas = []
    for i in range(3):
        resultado = obtener_float_valido(f"Introduce el resultado de la prueba #{i+1} (0-100): ")
        resultados_pruebas.append(resultado)
    
    # Crear el diccionario para la nueva pieza
    base_datos[num_serie] = {
        "tipo_componente": tipo_componente,
        "resultados_pruebas": resultados_pruebas,
        "estado": "Pendiente"
    }
    
    print(f"\nPieza '{num_serie}' registrada con éxito.")


def buscar_parte(base_datos):
    print("\nBúsqueda de Pieza")
    if not base_datos:
        print("El inventario está vacío. No hay piezas para buscar.")
        return

    num_serie = input("Introduce el S/N de la pieza a buscar: ").strip().upper()
    pieza = base_datos.get(num_serie)
    
    if pieza:
        print("\nDatos de la Pieza Encontrada")
        print(f"  Número de Serie: {num_serie}")
        print(f"  Tipo de Componente: {pieza['tipo_componente']}")
        print(f"  Resultados de Pruebas: {pieza['resultados_pruebas']}")
        print(f"  Estado: {pieza['estado']}")
    else:
        print(f"Error: No se encontró ninguna pieza con el S/N '{num_serie}'.")


def evaluar_parte(base_datos):
    print("\nEvaluación de Pieza")
    if not base_datos:
        print("El inventario está vacío. No hay piezas para evaluar.")
        return

    num_serie = input("Introduce el S/N de la pieza a evaluar: ").strip().upper()
    
    if num_serie in base_datos:
        resultados = base_datos[num_serie]["resultados_pruebas"]
        promedio = sum(resultados) / len(resultados)
        if promedio >= 90.0:
            base_datos[num_serie]["estado"] = "Aprobado"
        else:
            base_datos[num_serie]["estado"] = "Rechazado"
        print(f"\nEvaluación completa para '{num_serie}':")
        print(f"  Promedio de pruebas: {promedio:.2f}")
        print(f"  Nuevo estado: {base_datos[num_serie]['estado']}")
    else:
        print(f"Error: No se encontró ninguna pieza con el S/N '{num_serie}'.")


def ver_inventario(base_datos):
    print("\n--- Inventario de Control de Calidad ---")
    if not base_datos:
        print("El inventario está vacío.")
    else:
        for sn, datos in base_datos.items():
            print(f"S/N: {sn} - Tipo: {datos['tipo_componente']} - Estado: {datos['estado']}")


#? --- FUNCIÓN RECURSIVA Y SU GESTOR ---

def contar_componentes_recursivo(lista_partes, tipo_a_contar):
    #! Caso Base: Si la lista está vacía, no hay nada que contar.
    if not lista_partes:
        return 0

    #! Paso Recursivo:
    primera_parte = lista_partes[0]
    resto_lista = lista_partes[1:]
    
    #! Comprobar si la primera parte de la lista es del tipo buscado
    if primera_parte['tipo_componente'] == tipo_a_contar:
        #! Si coincide, suma 1 y sigue contando en el resto de la lista.
        return 1 + contar_componentes_recursivo(resto_lista, tipo_a_contar)
    else:
        #! Si no coincide, suma 0 y sigue contando en el resto de la lista.
        return 0 + contar_componentes_recursivo(resto_lista, tipo_a_contar)

def gestionar_conteo(base_datos):
    print("\nConteo de Componentes por Tipo")
    if not base_datos:
        print("El inventario está vacío. No hay nada que contar.")
        return
    tipo_a_contar = obtener_tipo_valido()
    lista_de_piezas = list(base_datos.values())
    total = contar_componentes_recursivo(lista_de_piezas, tipo_a_contar)
    print(f"\nResultado: Hay {total} pieza(s) del tipo '{tipo_a_contar}'.")


#! BUCLE PRINCIPAL DEL PROGRAMA

def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n" + "="*20)
    print(" Sistema de Control de Calidad")
    print("="*20)
    print("1. Registrar nueva pieza (registrar)")
    print("2. Buscar pieza por S/N (buscar)")
    print("3. Evaluar pieza (evaluar)")
    print("4. Ver inventario (ver_inventario)")
    print("5. Contar piezas por tipo (conteo)")
    print("6. Salir (salir)")
    print("="*20)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip().lower()

        if opcion in ("1", "registrar"):
            registrar_parte(base_de_partes)
        elif opcion in ("2", "buscar"):
            buscar_parte(base_de_partes)
        elif opcion in ("3", "evaluar"):
            evaluar_parte(base_de_partes)
        elif opcion in ("4", "ver inventario"):
            ver_inventario(base_de_partes)
        elif opcion in ("5", "conteo"):
            gestionar_conteo(base_de_partes)
        elif opcion in ("6", "salir"):
            print("\nCerrando sistema de QC...")
            break
        else:
            print("\nError: Opción no válida. Por favor, elige una de las disponibles.")

main()