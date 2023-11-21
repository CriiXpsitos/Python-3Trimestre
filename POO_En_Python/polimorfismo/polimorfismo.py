#polimorfismo (poli => muchas / morfos => cosas)

class Estudiante():
    def describir(self):
        print("Soy un estudiante")
        
class Profesor():
    def describir(self):
        print("Soy un profesor")
        
class Administrativo():
    def describir(self):
        print("Soy un administrativo")


def describirPersona(persona):
    persona.describir()

personas = Administrativo()
describirPersona(personas)

