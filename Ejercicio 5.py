personas = []
class Persona:
    nombre = ""
    padre = []
    madre = []
    esposa = []
    esposo = []
    hijos = []
    hermanos = []
    abuelo = []
    abuela = []
Juan = Persona()
Mariana = Persona()
Jorge = Persona()
Wendy = Persona()
Steve = Persona()
Iris = Persona()
Ada = Persona()
Isaac = Persona()
Elizabeth = Persona()
Niels = Persona()
Nicola = Persona()
personas.append(Juan)
personas.append(Mariana)
personas.append(Jorge)
personas.append(Wendy)
personas.append(Steve)
personas.append(Iris)
personas.append(Ada)
personas.append(Isaac)
personas.append(Elizabeth)
personas.append(Niels)
personas.append(Nicola)
Juan.nombre = "Juan"
Juan.padre.append("")
Juan.madre.append("")
Juan.esposa.append(Mariana)
Juan.hijos.append(Jorge)
Juan.hermanos.append("")
Juan.abuelo.append("")
Juan.abuela.append("")
Mariana.nombre = "Mariana"
Mariana.padre.append("")
Mariana.madre.append("")
Mariana.esposo.append(Juan)
Mariana.hermanos.append("")
Mariana.abuelo.append("")
Mariana.abuela.append("")
Jorge.nombre = "Jorge"
Jorge.padre.append(Juan)
Jorge.madre.append(Mariana)
Jorge.esposa.append(Wendy)
Jorge.hijos.append(Steve)
Jorge.hijos.append(Iris)
Jorge.hermanos.append(Elizabeth)
Jorge.hermanos.append(Ada)
Jorge.abuelo.append("")
Jorge.abuela.append("")
Wendy.nombre = "Wendy"
Wendy.padre.append("")
Wendy.madre.append("")
Wendy.esposo.append(Jorge)
Wendy.hijos.append(Steve)
Wendy.hijos.append(Iris)
Wendy.hermanos.append("")
Wendy.abuelo.append("")
Wendy.abuela.append("")
Ada.nombre = "Ada"
Ada.padre.append(Juan)
Ada.madre.append(Mariana)
Ada.esposo.append(Isaac)
Ada.hijos.append(Niels)
Ada.hijos.append(Nicola)
Ada.hermanos.append(Jorge)
Ada.hermanos.append(Elizabeth)
Ada.abuelo.append("Desconocida")
Ada.abuela.append("Desconocido")
Elizabeth.nombre = "Elizabeth"
Elizabeth.padre.append(Juan)
Elizabeth.madre.append(Mariana)
Elizabeth.hermanos.append(Jorge)
Elizabeth.hermanos.append(Ada)
Elizabeth.abuelo.append("")
Elizabeth.abuela.append("")
Steve.nombre = "Steve"
Steve.padre.append(Jorge)
Steve.madre.append(Wendy)
Steve.hermanos.append(Iris)
Steve.abuelo.append(Juan)
Steve.abuela.append(Mariana)
Iris.nombre = "Iris"
Iris.padre.append(Jorge)
Iris.madre.append(Wendy)
Iris.hermanos.append(Steve)
Iris.abuelo.append(Juan)
Iris.abuela.append(Mariana)
Isaac.nombre = "Isaac"
Isaac.padre.append("Desconocido")
Isaac.madre.append("Desconocido")
Isaac.esposa.append(Ada)
Isaac.hijos.append(Niels)
Isaac.hijos.append(Nicola)
Isaac.abuelo.append("Desconocido")
Isaac.abuela.append("Desconocido")
Niels.nombre = "Niels"
Niels.padre.append(Isaac)
Niels.madre.append(Ada)
Niels.hermanos.append(Nicola)
Niels.abuelo.append(Juan)
Niels.abuela.append(Mariana)
Nicola.nombre = "Nicola"
Nicola.padre.append(Isaac)
Nicola.madre.append(Ada)
Nicola.hermanos.append(Niels)
Nicola.abuelo.append(Juan)
Nicola.abuela.append(Mariana)
busqueda = input("Ingresa el nombre de un miembre de la familia para acceder a su árbol genealógico: ")
num = 0
for persona in personas:
    if persona.padre[0] == "":
        print("Inicio del árbol genealógico")
        break
    else:
        if persona.nombre == busqueda:
            print("Nombre: " + persona.nombre)
            print("Padre: " + persona.padre[num].nombre)
            print("Madre: " + persona.madre[num].nombre)
            print("Abuelo: " + persona.abuelo[num].nombre)
            print("Abuela: " + persona.abuela[num].nombre)
    num += 1
