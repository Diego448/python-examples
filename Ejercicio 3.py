class Empleado:
    nombre = ""
    puesto = ""
    salario = ""
#empleado1 = Empleado()
#empleado2 = Empleado()
#empleado3 = Empleado()
#empleado4 = Empleado()
empleadoX = Empleado()
empleados = []
empleados.append(empleadoX)
#empleados.append(empleado1)
#empleados.append(empleado2)
#empleados.append(empleado3)
#empleados.append(empleado4)
encontrado = 0
num = 0
nombre = ""
puesto = ""
salario = ""
f = open("Empleados.txt", 'a')
for i in range(1):
    empleados[i].nombre = input("Ingresa el nombre del empleado " + str(i) + ": ")
    f.write(empleados[i].nombre + "\n")
    empleados[i].puesto = input("Ingresa el puesto del empleado " + str(i) + ": ")
    f.write(empleados[i].puesto + "\n")
    empleados[i].salario = input("Ingresa el salario del empleado " + str(i) + ": ")
    f.write(empleados[i].salario + "\n")
sel = str(input("Ingresa el nombre del empleado para accesar a sus datos: "))
f.close()
f = open("Empleados.txt", 'r')
for line in f:
    num += 1
f.seek(0)
for i in range(0, num, 3):
    nombre = str(f.readline())
    nombre = nombre.rstrip()
    puesto = str(f.readline())
    puesto = puesto.rstrip()
    salario = str(f.readline())
    salario = salario.rstrip()
    if nombre == sel:
        print("Encontrado: ")
        print("Nombre: " + nombre)
        print("Puesto: " + puesto)
        print("Salario: $" + salario + ".00") 
#for i in range(4):
#    if empleados[i].nombre == sel:
#        print("Nombre: " + empleados[i].nombre)
#        print("Puesto: " + empleados[i].puesto)
#        print("Salario: " + empleados[i].salario)
#        encontrado = 1
#        break
#if encontrado != 1:
#    print("Empleado no encontrado")
f.close()
