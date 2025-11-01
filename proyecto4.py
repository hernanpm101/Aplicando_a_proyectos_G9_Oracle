"""
7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
Puedes apoyarte en la función map()
"""

nombres = ["juan", "MaRia", "JOSÉ"] 
apellidos = ["SILVA", "sosa", "Tavares"]

def concatenar_nombres_apellidos(nombres, apellidos):
    nombres_normalizados = list(map(lambda x: x.capitalize(), nombres))
    apellidos_normalizados = list(map(lambda x: x.capitalize(), apellidos))
    nombres_completos = list(map(lambda x, y: x + ' ' + y, nombres_normalizados, apellidos_normalizados))
    return nombres_completos

nombres_completos = concatenar_nombres_apellidos(nombres, apellidos)
print(nombres_completos)  


#output   ['Juan Silva', 'Maria Sosa', 'José Tavares']