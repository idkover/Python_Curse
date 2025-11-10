def apuntes():
    lista1=[1,2,3]
    lista2=[0]
    print(lista1)
    listanidada=[1,2,[3,4],5]
    print("Ultimo dato de la lista anidada",listanidada[-1]) 
    
    lista1.append(5) #! Añade al final de la lista un dato 
    lista1.remove(5) #! Elimina los datos "5" 
    lista1.pop(0) #! Elimina el dato que este almacenado en la direccion seleccionada 
    lista1.insert(3,10) #!inserta con esta redaccion (x, dato)
    lista1.clear() #! Borra el contenido de la lista 
    lista1.extend(lista2) #! Une dos listas
    print(f"Longitud de la lista: {len(lista1)}") #! Len muestra la cantidad de elementos almacenados en la lista 
    lista1.sort() #! Ordena de manera ascendente la lista
    lista1.reverse() #! Invierte el orden de los elementos de una lista 
    lista1.count(0) #! Contar cuantas veces esta un elemento en la lista 
    print("-"*20)
    lista1.remove("papas")


def main():

    a=int(input("Ingresa tu edad: "))
    g=input=("Ingresa tus 3 videojuegos favoritos: ")

def test():
    x=int(input("Introduzca el primer numero: "))

test()