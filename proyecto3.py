"""
6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

mayor nota  

menor nota  

media  

situación (Aprobado(a) o Reprobado(a))

Uso de la función  

Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.
"""


lista_notas = [8.5, 9.0, 6.0, 10.0]

def analisis_notas(notas):
    media = sum(notas) / len(notas)
    mayor_nota = max(notas)
    menor_nota = min(notas)
    situacion = 'Aprobado(a)' if media >= 7 else 'Reprobado(a)'
    return media, mayor_nota, menor_nota, situacion

media, mayor_nota, menor_nota, situacion = analisis_notas(lista_notas)

print(f"El estudiante obtuvo una media de {media}, con la mayor nota de {mayor_nota} puntos y la menor nota de {menor_nota} puntos y fue {situacion}.")