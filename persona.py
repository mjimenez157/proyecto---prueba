class Persona:
    nombre = "juan"
    edad = "18"
    
    
    def estudiar(self):
        self.estudiar = True
        return "persona que estudia..."

estudiante = Persona()
print(estudiante.nombre)
print(estudiante.estudiar())