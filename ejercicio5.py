texto = "pYthon, 2020. cursAda priMer, cuatRimestre pYthon pYthon pYthon pYthonpYthon"
texto_sin_caracteres = texto.replace(",","")
texto_sin_caracteres = texto_sin_caracteres.replace(".","")
texto_sin_caracteres = texto_sin_caracteres.lower()
texto_sin_caracteres = texto_sin_caracteres.split(" ")

texto_final=set(texto_sin_caracteres)

print(texto_final)
