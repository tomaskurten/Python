class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f'Se ha creado la película: {self.titulo}')
    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'


class Catalogo:
    peliculas = [] # Esta de objetos de la clase Pelicula
 # Constructor de clase
    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas
    def agregar(self, p): # p es un objeto Pelicula
        Catalogo.peliculas.append(p)
    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p) 

peli1=Pelicula("In bruges",123,2008)
# print(peli1)
peli2=Pelicula("Padrino",193,1972)
cat1=Catalogo([peli1])
cat1.agregar(peli2)
cat1.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))

cat1.mostrar()
print(cat1.peliculas[1])