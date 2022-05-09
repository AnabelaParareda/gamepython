print("Hello")


def calcular_dano(material):
    if(material == "madera"):
        return 1
    elif(material == "piedra"):
        return 2
    elif(material == "diamante"):
        return 5
    elif(material == "hierro"):
        return 3
    elif(material == "oro"):
        return 4
    else:
        return 4

#Clase de tipo espada


class Espada:
    def __init__(self, material, modelo3d):
        self.material = material
        self.mango = "Madera"
        self.modelo_3d = modelo3d
        self.attack_damage = calcular_dano(material)

    def imprimir_material(self):
        print(self.material)

    def atacar(self, mounstro):
        print(
            f"La espada de {self.material} atacó a {mounstro.nombre} y le hizo {self.attack_damage * -1} de daño")
        mounstro.esAtacado(self.attack_damage)


class Mounstro:
    def __init__(self, familia):
        nombre = input("Nombre: ")
        print(f"{nombre} nació como un nuevo mounstro.")
        self.vida = 5
        self.nombre = nombre
        self.familia = familia

    def tomar_pocion(self):
        vida_a_restaurar = 2
        print(
            f"{self.nombre} se tomó una poción y le restauro {vida_a_restaurar} de vida")
        self.vida += vida_a_restaurar

    def esAtacado(self, cantidad_dano):
        self.vida -= cantidad_dano
        if(self.vida <= 0):
            print(f"{self.nombre} murió")
            if(self.familia == True):
                print("y dejo a su familia atras")
            else:
                print("murio solo y nadie lo va a recordar")
        else:
            print(f"{self.nombre} dice - Auch!")


espadita = Espada("piedra", "archivo.3d")
espadita.imprimir_material()
mounstro = Mounstro(True)

turno = 0
while mounstro.vida > 0:
    print(f"Estas en el turno {turno}")
    print(f"La vida actual de {mounstro.nombre} es de {mounstro.vida}")
    accion = input("¿curar o atacar?: ")
    if(accion == "curar"):
        mounstro.tomar_pocion()
    elif(accion == "atacar"):
        espadita.atacar(mounstro)
    else:
        mounstro.tomar_pocion()

    turno += 1

print("JUEGO TERMINADO")
