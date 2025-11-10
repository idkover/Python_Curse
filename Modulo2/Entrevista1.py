import re  
from collections import Counter 

def contar_palabras(texto: str) -> dict:
    texto_min=texto.lower()
    palabras=re.findall(r'\b\w+\b', texto_min)
    conteo=Counter(palabras)
    return dict(conteo)

def procesar_y_guardar(archivo_entrada: str, archivo_salida: str, palabras_a_buscar: list):
    print(f"Iniciando procesamiento de '{archivo_entrada}'...")
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            texto_completo = f.read()

        conteo_total = contar_palabras(texto_completo)
        
        print("Conteo total de palabras completado")

        lineas_a_guardar=[]
        
        palabras_a_buscar_min=[p.lower() for p in palabras_a_buscar]

        for palabra in palabras_a_buscar_min:
            frecuencia=conteo_total.get(palabra, 0)
            
            lineas_a_guardar.append(f"{palabra}: {frecuencia}\n")
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.writelines(lineas_a_guardar)
            
        print(f"Resultados guardados en '{archivo_salida}'")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo de entrada: '{archivo_entrada}'")
        print("Por favor, asegúrate de que el nombre esté correcto y en la misma carpeta")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

#!Instrucciones de uso

# 1. Define el nombre del archivo de entrada
nombre_archivo_entrada="texto_original.txt" 

# 2. Define el nombre del archivo donde quieres guardar el resultado
nombre_archivo_salida="conteo_filtrado.txt"

# 3. La lista de palabras específicas que mencionaste
lista_palabras_filtrar=[
    "Dostoievski",
    "sinónimos",
    "Horiki",
    "humanos",
    "miedo",
    "palabras"
]


def main():
    #Creo un archivo con texto para ejemplo y pueda probar el programa 
    try:
        with open(nombre_archivo_entrada, 'x', encoding='utf-8') as f_ejemplo:
            f_ejemplo.write("""
            Este es un texto de ejemplo
            Hablaremos de Dostoievski y sus personajes humanos
            Los humanos sienten miedo
            Qué sinónimos de miedo conoces?
            Este texto no menciona a Horiki, pero sí usa varias palabras
            Palabras palabras palabras
            DOSTOIEVSKI (con mayúsculasdebe contar igual)
            """)
        print(f"Archivo de ejemplo '{nombre_archivo_entrada}' creado.")
    except FileExistsError:
        pass
        

    procesar_y_guardar(nombre_archivo_entrada, nombre_archivo_salida, lista_palabras_filtrar)

main()