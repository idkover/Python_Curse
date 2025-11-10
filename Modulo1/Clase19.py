import os

TIPOS_ENTRADA_VALIDOS = ("Observacion", "Prueba", "Error", "Mantenimiento")
NOMBRE_ARCHIVO = "laboratorio.txt"

def registrar_entrada():
    print("\nRegistrar Nueva Entrada")
    while True:
        print(f"Tipos de entrada válidos: {', '.join(TIPOS_ENTRADA_VALIDOS)}")
        tipo_entrada = input("Introduce el tipo de entrada: ").strip().capitalize()
        
        if tipo_entrada in TIPOS_ENTRADA_VALIDOS:
            break
        else:
            print(f"Error: '{tipo_entrada}' no es un tipo válido. Inténtalo de nuevo.")
    descripcion = input("Introduce la descripción de la entrada: ").strip()
    try:
        with open(NOMBRE_ARCHIVO, 'a', encoding='utf-8') as archivo:
            archivo.write(f"TIPO: {tipo_entrada} - DESCRIPCIÓN: {descripcion}\n")
        print("\nEntrada registrada con éxito!\n")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}\n")


def ver_log():
    print("\nContenido del Cuaderno de Laboratorio")
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            if not contenido:
                print("El log está vacío. Registra una nueva entrada!\n")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El log está vacío o no se ha creado todavía\n")
    except IOError as e:
        print(f"\nError al leer el archivo: {e}\n")


def main():
    while True:
        # Menú de Opciones
        print("="*20)
        print("  Cuaderno de Laboratorio Digital 🔬")
        print("="*20)
        print("Opciones disponibles:")
        print("1.- registrar: Añadir una nueva entrada")
        print("2.- ver_log:   Mostrar todas las entradas")
        print("3.- salir:     Cerrar el programa")
        print("-"*20)
        
        opcion = input("Elige una opción: ").strip().lower()
        
        if opcion == "registrar" or opcion=="1":
            registrar_entrada()
        elif opcion=="ver_log" or opcion=="ver log" or opcion=="2":
            ver_log()
        elif opcion=="salir" or opcion=="3":
            print("\nHasta luego! Cerrando el cuaderno")
            break 
        else:
            print(f"\nOpción '{opcion}' no reconocida. Por favor, elige una opción válida\n")

main()