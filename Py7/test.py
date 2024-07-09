from gato import Gato
from perro import Perro
from animal import Animal


# Bloque Ppal
def __main__():
    # a1= Animal() # TypeError: Can't instantiate abstract class Animal
    # a1.emitir_sonido()
    g1= Gato()
    g1.mover()
    g1.emitir_sonido()
    p1= Perro()
    p1.emitir_sonido()
    g1.emitir_sonido()
    

if __name__ == "__main__":
    __main__()