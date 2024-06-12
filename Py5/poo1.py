# class Persona:
#     piernas = 2
    
# juan = Persona()
# print(juan)
# print(juan.piernas)
# maria=Persona()
# print(maria)
# print(maria.piernas)

class Perro:
    genero="canino"
    contador=0
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        Perro.contador+=1
        self.id=Perro.contador
        
    def __str__(self):
        return f'Mi nombre es: {self.nombre}, ID: {self.id}, y tengo {self.edad}'
    
    def cumplir(self):
        self.edad+=1
    
    def __del__(self):
        Perro.contador-=1
# perro1=Perro("Ron",3)
# perro2=Perro("Luna",10)
# perro3=Perro("Lola",12)
# print(perro1.nombre)
# print(perro2.nombre)
# # print(perro1.genero)
# # print(perro2.genero)
# print(perro3.nombre)
# print(perro1.edad)
# print(perro1)
# # print(perro2)
# # print(perro3)
# perro1.cumplir()
# perro1.cumplir()
# perro1.cumplir()
# print(perro1)

def cargar_mascotas():
    lista=[]
    nombre=input("Ingrese nombre: ")
    while nombre!="":
        edad=int(input("Ingrese edad: "))
        perro=Perro(nombre,edad)
        lista.append(perro)
        nombre=input("Ingrese nombre: ")
    return lista

def mostrar_lista(lista):
    for elem in lista:
        print(elem)

mascotas=cargar_mascotas()
# print(mascotas)
mostrar_lista(mascotas)
# print(mascotas[1].contador)
del mascotas[3]
mostrar_lista(mascotas)
