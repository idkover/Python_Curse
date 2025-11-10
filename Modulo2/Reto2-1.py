class Componente:
    def __init__(self, numero_serie, tipo_componente, costo):
        self.numero_serie=numero_serie
        self.tipo=tipo_componente
        self.costo=costo
        
        self.historial_revisiones=[]  
        self.esta_activo=True         

#! Fin de definicion

c1 = Componente(numero_serie="MTR-1001", tipo_componente="Motor", costo=550.75)
c2 = Componente(numero_serie="SNR-2050", tipo_componente="Sensor", costo=80.20)

c1.historial_revisiones.append("2025-10-25")
c2.historial_revisiones.append("2025-10-28")

c2.esta_activo = False

print("-"*20)
print("Reporte de Componentes de Fábrica")
print("-"*20)

#! C1
print("\nFicha del Componente 1")
print(f"Numero de Serie: {c1.numero_serie}")
print(f"Tipo: {c1.tipo}")
print(f"Costo: ${c1.costo}")
print(f"Historial de Revisiones: {c1.historial_revisiones}")
print(f"Esta activo?: {c1.esta_activo}")

#! C2
print("\nFicha del Componente 2")
print(f"Numero de Serie: {c2.numero_serie}")
print(f"Tipo: {c2.tipo}")
print(f"Costo: ${c2.costo}")
print(f"Historial de Revisiones: {c2.historial_revisiones}")
print(f"¿Esta activo?: {c2.esta_activo}")