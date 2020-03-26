tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista1 = []
lista2 = []
for i in tam:
    nom, pos, ub = i.partition(" ")
    pos1 = (int(ub.split(',')[0]), int(ub.split(',')[1]))
    if pos1[0] > 30:
        lista1.extend([nom, pos1])
    else:
        lista2.extend([nom, pos1])
print(lista1, lista2)
