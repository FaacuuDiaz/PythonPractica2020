texto = "python 2020 cursada primer cuatrimestre"
texto_separado=texto.lower().split(' ')
palabra = input("ingrese la palabra \n").lower()
contador=0
for i in texto_separado:
    if palabra == i:
        contador+=1
print("la cantidad de palabras iguales son", contador)        