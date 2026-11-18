class Personaje:

    def __init__(self, nombre, vida, danyo):
        self.nombre = nombre
        self.vidaMax = vida
        self.vida = vida
        self.danyo = danyo

    def atacar(self, objetivo):
        if not self.estaVivo():
            print(f"{self.nombre} está derrotado, por lo que no puede atacar.")
            return False
        print(f"{self.nombre} ataca a {objetivo.nombre} haciendo {self.danyo} de daño")
        objetivo.recibirDanyo(self.danyo)
        return True


    def recibirDanyo(self, danyo):
        if not self.estaVivo():
            print(f"{self.nombre} está derrotado, por lo que no puede recibir daño.")
            return False
        self.vida -= danyo
        if self.vida < 0:
            self.vida = 0


    def estaVivo(self):
        return self.vida > 0
    
    def mostrarEstado(self):
        print(f"{self.nombre} - Vida: {self.vida}/{self.vidaMax}")

