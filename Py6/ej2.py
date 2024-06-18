class Bebidas:
 def __init__(self):
    self.__bebida = 'Naranja'
 @property
 def favorita(self):
    return f"La bebida preferida es: {self.__bebida}"
 @favorita.setter
 def favorita(self, bebida):
    if bebida!="" and type(bebida)==str:
        self.__bebida = bebida
    else:
        print("ERROR, INGRESE STRING NO VACIO!!")
    
# Programa principal
obj1 = Bebidas()
print(obj1.favorita)
obj1.favorita = ""
obj1.favorita = 2
obj1.favorita = "Pomelo"
print(obj1.favorita)