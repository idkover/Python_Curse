def main():
    x=int(input("Introduzca el primer numero: "))
    y=int(input("Introduzca el segundo numero: "))
    
    s=float(x+y)
    r=float(x-y)
    m=float(x*y)
    d=float(x / y)
    modulo1=float(x % 2)
    modulo2=float(y % 2)
    pot1=float(x ** 3)
    pot2=float(y ** 3)

    print(f"La suma es igual a: {s}")
    print(f"La resta es igual a: {r}")
    print(f"La multiplicacion es igual a: {m}")
    print(f"La division es igual a: {d}")
    print(f"El modulo 2 del primer numero es: {modulo1} y del segundo es: {modulo2}")
    print(f"La potencia del primer numero al cubo es: {pot1} y la potencia del segundo numero al cubo es: {pot2}")

    a=int(input("Excelente! de nueva cuanta ingresa un numero para las siguientes operaciones: "))
    b=int(input("El segundo: "))

    a += 2
    b -= 13

    print("Asignacion suma con el primer numero: ",a)
    print("Asignacion resta con el segundo numero: ",b)
    print(f"igualdad: {a == b}")
    print(f"desigualdad: {a!=b}")
    print(f"mayor que: {a>b}")
    print(f"menor que: {a<b}")

main()