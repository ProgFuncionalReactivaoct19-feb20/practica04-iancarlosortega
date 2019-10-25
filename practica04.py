"""
	Practica04:
	@iancarlosortega
"""

import codecs
import json

archivo = codecs.open("datos.txt")

lineas = archivo.readlines()

lineas_diccionario = [json.loads(l) for l in lineas]

resultado = list(filter(lambda x: list(x.items())[1][1]>3, lineas_diccionario))

resultado2 = list(filter(lambda x: list(x.items())[0][1]=="Nigeria",lineas_diccionario))

lista = list(map(lambda x: list(x.items())[2][1], lineas_diccionario))

maximo = max(lista)

minimo = min(lista)

resultado3 = list(filter(lambda x: list(x.items())[2][1]==maximo, lineas_diccionario))

resultado4 = list(filter(lambda x: list(x.items())[2][1]==minimo, lineas_diccionario))

print("Jugadores con mas de 3 goles:\n\n",resultado,"\n")
print("Jugadores provenientes de Nigeria:\n\n",resultado2,"\n")
print("Jugador mas alto:\n\n",resultado3,"\n")
print("Jugador mas pequeño:\n\n",resultado4,"\n")