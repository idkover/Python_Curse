def eliminar_duplicados_ordenados(lista_original: list) -> list:
    vistos=set()
    lista_sin_duplicados=[]
    for elemento in lista_original:
        if elemento not in vistos:
            lista_sin_duplicados.append(elemento)
            vistos.add(elemento)
    return lista_sin_duplicados

lista_datos=[
    1, 8, 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 
    2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3
]

resultado=eliminar_duplicados_ordenados(lista_datos)

print(f"Lista Original: \n{lista_datos}")
print("-" * 20)
print(f"Lista Sin Duplicados (en orden): \n{resultado}")