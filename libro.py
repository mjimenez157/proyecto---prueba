class Libro:
    nombre = "100 años de soledad"
    autor = "gabriel garcia marquez"
    paginas = 500
    editorial = "alfaguara"
    
    def leer(self):
        self.leer = True
        return "persona que lee..."

novela = Libro()
print(novela.nombre)
print(novela.leer())