frase='ejercicio dos de la Practica tres Python veiNte veinte'

frase=frase.lower()
frase=frase.split(" ")
diccionario_de_palabras={}
for palabra in frase:
    if len(palabra) in diccionario_de_palabras.keys():
        diccionario_de_palabras[len(palabra)].append(palabra)
    else:
        diccionario_de_palabras[len(palabra)]=[palabra]

print(diccionario_de_palabras)