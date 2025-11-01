"""
8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]

goles_recibidos = [1, 2, 2, 1, 3]

Texto probablemente mostrado:

La puntuación del equipo fue puntos y su rendimiento fue desempeno%"
"""

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

def calcula_puntos(goles_marcados, goles_recibidos):
  puntos = 0
  total_juegos = len(goles_marcados)
  puntuacion_maxima = total_juegos * 3

  for i in range(total_juegos):
    if goles_marcados[i] > goles_recibidos[i]:
      puntos += 3
    elif goles_marcados[i] == goles_recibidos[i]:
      puntos += 1

  desempeno = (puntos / puntuacion_maxima) * 100 if puntuacion_maxima > 0 else 0
  return puntos, desempeno

puntos, desempeno = calcula_puntos(goles_marcados, goles_recibidos)

print(f'La puntuación del equipo fue {puntos} y su rendimiento fue {desempeno:.2f}%')