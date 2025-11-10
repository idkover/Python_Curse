import string 
def contar_palabras_especificas(archivo_entrada, archivo_salida, palabras_a_buscar):
    print(f"Iniciando el conteo de palabras del archivo: '{archivo_entrada}'...")

    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            texto_completo = f.read()
        texto_en_minusculas = texto_completo.lower()
        texto_limpio = ""
        for caracter in texto_en_minusculas:
            if caracter not in string.punctuation and caracter not in "¡¿": # Añadimos puntuación en español
                texto_limpio += caracter
            else:
                texto_limpio += " " # Reemplazamos la puntuación por un espacio


        lista_de_palabras = texto_limpio.split()


        palabras_a_buscar_lower = [palabra.lower() for palabra in palabras_a_buscar]
        

        conteo_de_palabras = {palabra: 0 for palabra in palabras_a_buscar_lower}

        for palabra in lista_de_palabras:
            # Si la palabra está en nuestra lista de interés, incrementamos su contador.
            if palabra in conteo_de_palabras:
                conteo_de_palabras[palabra] += 1
        
        # --- 6. Guardar los resultados en el archivo de salida ---
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write("Conteo final de palabras:\n")
            f.write("-------------------------\n")
            for palabra, cantidad in conteo_de_palabras.items():
                linea = f"{palabra}: {cantidad}\n"
                f.write(linea)
        
        print(f"¡Éxito! El resultado se ha guardado en '{archivo_salida}'.")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'. Asegúrate de que el archivo existe.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


# --- INICIO DEL PROGRAMA ---
if __name__ == "__main__":
    # Define el nombre de los archivos
    archivo_de_texto = "texto_entrada.txt"
    archivo_de_resultados = "conteo_salida.txt"

    # Define la lista de palabras específicas que quieres contar
    palabras_objetivo = [
        "Dostoievski",
        "sinónimos",
        "Horiki",
        "humanos",
        "miedo",
        "palabras"
    ]

    # Llama a la función principal con los parámetros definidos
    contar_palabras_especificas(archivo_de_texto, archivo_de_resultados, palabras_objetivo)