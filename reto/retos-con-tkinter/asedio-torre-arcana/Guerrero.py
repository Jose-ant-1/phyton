from Personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, danyo=12)
        self.cargas = 2
        self.danyoHabilidad = 24

    def habilidadEspecial(self, objetivo):
        if not self.estaVivo():
            return False, f"{self.nombre} está derrotado, por lo que no puede usar habilidades."

        if self.cargas <= 0:
            return False, "No quedan cargas para usar Golpe Poderoso."

        self.cargas -= 1
        objetivo.recibirDanyo(self.danyoHabilidad)
        return True, f"{self.nombre} usa Golpe Poderoso contra {objetivo.nombre}, infligiendo {self.danyoHabilidad} de daño."

    def getRecursoTexto(self):
        return f"Cargas: {self.cargas}/2"

    def mostrarEstado(self):
        return f"[Guerrero: {self.nombre}] - Vida: {self.vida}/{self.vidaMax} | Cargas: {self.cargas}"
