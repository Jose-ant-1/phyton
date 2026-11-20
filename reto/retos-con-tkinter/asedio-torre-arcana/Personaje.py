class Personaje:
    def __init__(self, nombre, vida, danyo):
        self.nombre = nombre
        self.vidaMax = vida
        self.vida = vida
        self.danyo = danyo

    def atacar(self, objetivo):
        if not self.estaVivo():
            return False, f"{self.nombre} está derrotado y no puede atacar."
        objetivo.recibirDanyo(self.danyo)
        return True, f"{self.nombre} ataca a {objetivo.nombre} haciendo {self.danyo} de daño."

    def recibirDanyo(self, danyo):
        self.vida -= danyo
        if self.vida < 0:
            self.vida = 0

    def estaVivo(self):
        return self.vida > 0

    def mostrarEstado(self):
        return f"{self.nombre} - Vida: {self.vida}/{self.vidaMax}"
