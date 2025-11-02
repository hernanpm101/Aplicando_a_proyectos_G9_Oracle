"""
9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

Texto probablemente mostrado:

Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde Recife costaría [gastos] reales.


"""

costo_diario_hotel = 150
consumo_gasolina_km_por_litro = 14
precio_gasolina_por_litro = 5
gastos_alimentacion_ciudades = [200, 400, 250, 300] # Salvador, Fortaleza, Natal, Aracaju
distancias_ciudades_km = [850, 800, 300, 550] # Salvador, Fortaleza, Natal, Aracaju
ciudades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']


def calcular_gastos_hotel(costo_diario_hotel, dias_alojamiento):
  gastos = costo_diario_hotel * dias_alojamiento
  return gastos

def calcular_gastos_gasolina(distancia_km, consumo_gasolina_km_por_litro, precio_gasolina_por_litro):
  litros_gasolina_total = distancia_km / consumo_gasolina_km_por_litro
  gasto_gasolina = litros_gasolina_total * precio_gasolina_por_litro * 2 # Ida y vuelta
  return gasto_gasolina

def calcular_gastos_paseo(gastos_alimentacion_diarios, dias_alojamiento):
  gasto_paseo = gastos_alimentacion_diarios * dias_alojamiento
  return gasto_paseo

# Obtener entrada del usuario
dias_alojamiento = int(input("Ingrese el número de días de alojamiento: "))
ciudad = input("Ingrese la ciudad de destino (Salvador, Fortaleza, Natal, Aracaju): ")

# Encontrar el índice de la ciudad elegida para obtener la distancia y gastos diarios correctos
try:
    indice_ciudad = ciudades.index(ciudad)
    distancia = distancias_ciudades_km[indice_ciudad]
    gastos_alimentacion_diarios = gastos_alimentacion_ciudades[indice_ciudad]
except ValueError:
    print("Ciudad no válida. Por favor, elija entre Salvador, Fortaleza, Natal, o Aracaju.")
    exit()


# Calcular gastos usando las funciones
gastos_hotel = calcular_gastos_hotel(costo_diario_hotel, dias_alojamiento)
gastos_gasolina = calcular_gastos_gasolina(distancia, consumo_gasolina_km_por_litro, precio_gasolina_por_litro)
gastos_paseo = calcular_gastos_paseo(gastos_alimentacion_diarios, dias_alojamiento)

# Calcular gastos totales
gastos_totales = gastos_hotel + gastos_gasolina + gastos_paseo


# Imprimir el resultado
print(f"Con base en los gastos definidos, un viaje de {dias_alojamiento} días a {ciudad} desde Recife costaría {gastos_totales:.2f} reales.")


"""
OUTPUT:
Ingrese el número de días de alojamiento: 3
Ingrese la ciudad de destino (Salvador, Fortaleza, Natal, Aracaju): Salvador
Con base en los gastos definidos, un viaje de 3 días a Salvador desde Recife costaría 1657.14 reales.
"""