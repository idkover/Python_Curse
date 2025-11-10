
#! Clases y funciones
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        #Atributos públicos
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        #Atributos privados
        self._encendido = False

    def arrancar(self):
        if not self._encendido:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba en marcha")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado")
        else:
            print(f"El {self.marca} {self.modelo} ya estaba apagado")

    def get_kilometraje(self):
        return self.kilometraje

    def mostrar_info_base(self):
        print(f"Vehiculo: {self.marca} {self.modelo}, Año: {self.anio}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def conducir(self, km):
        if self._encendido:
            self.kilometraje += km
            print(f"Conduciendo {km} km")
        else:
            print("Error: El coche debe estar arrancado para conducir")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0

    def cargar(self, kilos):
        carga_potencial = self.__carga_actual_kg + kilos
        if carga_potencial <= self.capacidad_carga_kg:
            self.__carga_actual_kg = carga_potencial
            print(f"Carga exitosa, carga actual: {self.__carga_actual_kg} kg")
        else:
            print("Error: Sobrecarga")
            print(f"(Intento de añadir {kilos}kg a {self.__carga_actual_kg}kg capacidad máx: {self.capacidad_carga_kg}kg)")


    def descargar(self, kilos):
        if (self.__carga_actual_kg - kilos) >= 0:
            self.__carga_actual_kg -= kilos
            print(f"Descarga exitosa carga actual: {self.__carga_actual_kg} kg")
        else:
            print(f"Error: No se puede descargar {kilos} kg carga actual: {self.__carga_actual_kg} kg")

    def get_carga_actual(self):
        return self.__carga_actual_kg


#!Programa Principal

def main():
    
    print("Probando el Coche")
    
    #todo 1. Crear un objeto Coche
    mi_coche = Coche(marca="Toyota", modelo="Corolla", anio=2023, num_puertas=4)
    mi_coche.mostrar_info_base()
    print(f"Puertas: {mi_coche.num_puertas}")

    #todo 2. Prueba de conducción (debe fallar)
    print("\nIntentando conducir apagado:")
    mi_coche.conducir(50)

    #todo 3. Arrancar
    print("\nArrancando:")
    mi_coche.arrancar()

    #todo 4. Conducir 100 km
    print("\nConduciendo:")
    mi_coche.conducir(100)

    #todo 5. Apagar
    print("\nApagando:")
    mi_coche.apagar()

    #todo 6. Imprimir kilometraje final
    print(f"** Kilometraje final del coche: {mi_coche.get_kilometraje()} km **")
    print("\n" + "="*20 + "\n")
    print("Probando el Camión")


    #! 1. Crear un objeto Camion
    mi_camion = Camion(marca="Volvo", modelo="FH16", anio=2022, capacidad_carga_kg=5000)
    mi_camion.mostrar_info_base()
    print(f"Capacidad máxima: {mi_camion.capacidad_carga_kg} kg")
    #! 2. Cargar 3000 kg
    print("\nCargando 3000 kg:")
    mi_camion.cargar(3000)
    #! 3. Intentar cargar 3000 kg más (debe fallar)
    print("\nIntentando cargar 3000 kg más (debería fallar):")
    mi_camion.cargar(3000)
    #! 4. Descargar 1000 kg
    print("\nDescargando 1000 kg:")
    mi_camion.descargar(1000)
    #! 5. Imprimir carga actual
    print(f"** Carga final del camión: {mi_camion.get_carga_actual()} kg **")
main()