tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lista_coordenadas=[]

for elemento in tam:
    img,coord = elemento.split(" ")
    coord=coord.split(",")
    coord=int(coord[0]),int(coord[1])
    lista_coordenadas.append(coord)

#lista_coordenadas.sort()
print(sorted(lista_coordenadas,key=lambda x: x[1]))
#print(lista_coordenadas)

