def calcular_puntuacion_skater(notas):
    """
    Calcula la puntuación total de un skater sumando todas las notas recibidas.
    
    Args:
        notas (list): Lista de 5 notas ingresadas por los jueces.
        
    Returns:
        float: Puntuación total del atleta.
    """
    # Suma todos los elementos de la lista de notas.
    puntuacion_total = sum(notas)
    return puntuacion_total

# 1. Inicializar una lista vacía para almacenar las notas
notas_jueces = []
numero_de_notas = 5

print("🏁 ¡Bienvenido al sistema de cálculo de notas para skaters! 🛹")
print(f"Por favor, ingrese las {numero_de_notas} notas otorgadas por los jueces.")

# 2. Bucle para solicitar las 5 notas
for i in range(numero_de_notas):
    while True:
        try:
            # Solicitar la nota. Se usa i+1 para mostrar el número de nota (de 1 a 5).
            nota = float(input(f"Ingrese la Nota #{i+1} (ej. 8.5): "))
            
            # 3. Validar que la nota sea un valor positivo
            if nota >= 0:
                notas_jueces.append(nota)
                break  # Sale del bucle 'while True' si la entrada es válida
            else:
                print("⚠️ Error: La nota no puede ser un valor negativo. Intente de nuevo.")
        except ValueError:
            # Captura un error si el usuario ingresa texto en lugar de un número
            print("⚠️ Error: Entrada no válida. Por favor, ingrese solo números (pueden ser decimales).")

# 4. Llamar a la función para calcular el resultado final
puntuacion_final = calcular_puntuacion_skater(notas_jueces)

# 5. Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"Notas registradas: {notas_jueces}")
print(f"Puntuación Total del Atleta: **{puntuacion_final:.2f}** puntos")