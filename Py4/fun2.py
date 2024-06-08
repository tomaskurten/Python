# # def dividir(num1,num2=0):
# #     resultado=num2/num1
    
# #     # print(resultado)
# #     return resultado
    
# # print(dividir(num2=3,num1=5))
# # print(dividir(5,3))

# # print(dividir(1000000,9999))


# # def sumar(a,b):
# #     resultado=a+b
# #     if resultado>10:
# #         mensaje= "mayor a 10"
# #     else:
# #         mensaje= "menor a 10"
# #     return mensaje
    

# # print(sumar(3,4))
# # print(sumar(3,44))


# def calcular(n = 1):
#  tabla = []
#  for i in range(0,11):
#     tabla.append(f"{n}x{i}={n*i}")
#  return tabla

# # Muestra en terminal todas las tablas
# def calcular_todas():
#  for i in range(0,11):
#     print(f"Tabla del {i}:")
#     tabla = calcular(i)
#     for j in tabla:
#         print(j)
#     print("*"*10)
 
# #Programa principal
# # print(calcular(2))
# # calcular(0)
# # calcular(1)
# # calcular(2)
# # calcular(3)
# print(calcular_todas())


# funciones lambda
# lista=[1,1]
cuadrado = lambda x: x ** 2
# print(cuadrado(4))
# lista[0] = lambda x: x ** 2
# print(lista)
# es_par=lambda num:num%2==0
# print(es_par(2))
# print(es_par(5))

numeros=[1,3,45]
elevados=list(map(cuadrado,numeros))
print(elevados)
