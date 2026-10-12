class Pokemon:
    contador = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.contador += 1
        print("se creo el pokemn " + self.nombre)

    def __del__(self):
        Pokemon.contador -= 1
        print("el pokemon fue borrado " + self.nombre)

    def mostrar_info(self):
        print("--- datos del pokemon ---")
        print("nombre: " + self.nombre)
        print("tipo: " + self.tipo)
        print("nivel: " + str(self.nivel))
        print("ataque: " + str(self.ataque))
        print("defensa: " + str(self.defensa))
        print("salud: " + str(self.salud))

    def entrenar(self, *args):
        self.nivel += 1
        if len(args) == 0:
            self.ataque += 5
            self.defensa += 5
            self.salud += 10
        else:
            for arg in args:
                if arg == "ataque":
                    self.ataque += 10
                elif arg == "defensa":
                    self.defensa += 10
                elif arg == "salud":
                    self.salud += 20
        print("el pokin subio de nivel")

    def atacar(self, objetivo):
        daño = self.ataque - objetivo.defensa
        if daño < 0:
            daño = 1
        objetivo.salud -= daño
        print("el pokemon " + self.nombre + " ataco a " + objetivo.nombre)
        print("vida restante de " + objetivo.nombre + ": " + str(objetivo.salud))

    @classmethod
    def total_pokemons(cls):
        print("total de pokemones creados: " + str(cls.contador))