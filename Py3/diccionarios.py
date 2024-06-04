# diccionario={"hola":"Tomas", 345:"kurten","p":3}
# print(diccionario[345])
# diccionario[345]=True
# print(diccionario[345])


diccionario = {"primero": 'uno', True:'dos', 345345:'tres'}
print(diccionario.keys())
# for i in diccionario.keys():
#  print(diccionario[i])
for clave, valor in diccionario.items():
    print(clave, ':', valor, end= '; ')
