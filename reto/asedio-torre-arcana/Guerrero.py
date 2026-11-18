from Personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre):
        super().__init__(nombre, vida = 70, danyo = 12)
        self.cargas = 2
        self.danyoHabilidad = 24

    def habilidadEspecial(self, objetivo):
        if not self.estaVivo():
            print(f"{self.nombre} está derrotado, por lo que no puede usar habilidades")
            return False

        if self.cargas <= 0:
            print(f"No quedan cargas para usar golpe poderoso")
            return False

        self.cargas -= 1
        print(f"{self.nombre} usa golpe poderoso contra {objetivo.nombre}, inflingiendo {self.danyoHabilidad} de daño")        
        objetivo.recibirDanyo(self.danyoHabilidad)
        return True

    def mostrarEstado(self):
        print(f"[Guerrero: {self.nombre}] - Vida: {self.vida}/{self.vidaMax} | Cargas: {self.cargas}")
        

