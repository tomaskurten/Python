class Padre: # Superclase
 def __init__(self):
    self.apellido = "Volpin"
 def llevar(self):
    print("Papá me lleva al colegio.")

class Madre: # Superclase 2
 def programar(self):
    print("Mamá programa en Python.")

class Hijo(Padre,Madre): # Subclase
 def estudiar(self):
    print("Estoy en el colegio.")
    
# hijo1 = Hijo() # Instanciamos hijo1
# hijo1.llevar() # Papá me lleva al colegio.
# hijo1.estudiar() # Estoy estudiando
# print(hijo1.apellido) 

# padre1=Padre()
# padre1.llevar()
# print(padre1.apellido)

hijo1=Hijo()
print(hijo1.apellido)
hijo1.estudiar()
hijo1.llevar()
hijo1.estudiar()