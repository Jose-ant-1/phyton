from Personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=50, danyo=8)
        self.mana = 30
        self.costeMana = 15
        self.danyoHabilidad = 20

    def habilidadEspecial(self, objetivo):
        if not self.estaVivo():
            return False, f"{self.nombre} está derrotado, por lo que no puede usar habilidades."

        if self.mana < self.costeMana:
            return False, f"No hay suficiente maná. Tienes {self.mana} y necesitas {self.costeMana}."

        self.mana -= self.costeMana
        objetivo.recibirDanyo(self.danyoHabilidad)
        return True, f"{self.nombre} usó Bola de Fuego contra {objetivo.nombre}, infligiendo {self.danyoHabilidad} de daño."

    def getRecursoTexto(self):
        return f"Maná: {self.mana}/30"

    def mostrarEstado(self):
        return f"[Mago: {self.nombre}] - Vida: {self.vida}/{self.vidaMax} | Maná: {self.mana}"
