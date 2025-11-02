"""
10 - Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP). Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda se centra en el análisis del patrón de comportamiento de las personas al escribir palabras de esta cantidad de caracteres o más.

Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.

Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para probar el código.
"""

# Solicitando una frase y separándola por espacios. Usando replace para cambiar
# puntuaciones por espacios.
frase = input("Escribe una frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando la frase en formato de lista, pasando a la lista tamaño
# solo las palabras con 5 o más caracteres e imprimiéndola en pantalla
tamano = list(filter(lambda x: len(x) >= 5, frase))
print(tamano)


"""
OUTPUT:
Escribe una frase: Argentina va a selir campeon del mundo!!!!
['Argentina', 'selir', 'campeon', 'mundo']
"""

