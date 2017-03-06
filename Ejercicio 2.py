cantidadDias = []
rangoA = []
rangoB = []
diaAño = 0
mes = 0
diaMes = 0
grupo = 0
cantidadMiembros = []
rangoA.append(0)
rangoB.append(0)
rangoA.append(1)
rangoB.append(2)
cantidadDias.append(0)
for i in range(1, 25):
    cantidadDias.append(i + 1)
for i in range(2, 25):
    rangoA.append(rangoB[i - 1] + 1)
    rangoB.append(rangoA[i] + (cantidadDias[i] - 1))
cantidadDias.append(13)
rangoA.append(351)
rangoB.append(360)
mes = input("Ingresa el mes: ")
diaMes = input("Ingresa el dia: ")
mes = int(mes)
diaMes = int(diaMes)
if mes > 12:
    mes = 12
if diaMes > 30:
    diaMes = 30
if mes < 1:
    mes = 1
if diaMes < 1:
    diaMes = 1
if mes == 1:
    diaAño = diaMes
if mes > 1:
    diaAño = mes*30 + diaMes
for i in range(1, 26):
    if diaAño >= rangoA[i] and  diaAño <= rangoB[i]:
        grupo = i
        cantidadMiembros = i + 1
        break
print("Fecha: " + str(mes) + "/" + str(diaMes))
print("Grupo: " + str(grupo))
print("Numero de integrantes: " + str(cantidadMiembros))
