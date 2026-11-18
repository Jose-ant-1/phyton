from Personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida = 50, danyo = 8)
        self.mana = 30
        self.costeMana = 15
        self.danyoHabilidad = 20

    def habilidadEspecial(self, objetivo):
        if not self.estaVivo():
            print(f"{self.nombre} está derrotado, por lo que no puede usar habilidades")
            return False
        
        if self.mana < self.costeMana:
            print(f"No hay suficiente maná. Tienes {self.mana}")
            return False

        self.mana -= self.costeMana
        print(f"{self.nombre} usó Bola de fuego a {objetivo.nombre} haciendo {self.danyoHabilidad}")
        objetivo.recibirDanyo(self.danyoHabilidad)
        return True

    def mostrarEstado(self):
        print(f"[Mago: {self.nombre}] - Vida: {self.vida}/{self.vidaMax} | Maná: {self.mana}")
        


