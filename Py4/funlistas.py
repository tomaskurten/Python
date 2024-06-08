def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i])
        
def duplicar_lista(lista):
    for i in range(len(lista)):
        lista[i]*=2
    print(lista)


#main
numeros=[1,4,5,6]
palabras=["perro","naranja","auto"]

# mostrar_lista(numeros)
# mostrar_lista(palabras)
# duplicar_lista(numeros)
# duplicar_lista(palabras)

# print(numeros)
# print(palabras)

duplicar_lista(numeros[:])
print(numeros)