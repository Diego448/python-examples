import random
jgl = 0
jgp = 0
cant = 0
m = 0
print("Ingresa el numero de juegos: ")
cant = int(input())
print(cant)
for i in range(cant):
    rand = random.randint(0, 1)
    print(rand)
    if rand == 1:
        jgl += 1
    if rand == 0:
        jgp += 1
print("Juegos ganados Laura: ", jgl)
print("Juegos ganados Pedro: ", jgp)
