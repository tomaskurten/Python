# def imprimir():
#     print("Hola desde funcion")

# imprimir()


# def sumar(num1=0,num2=0):
#     resultado=num1+num2
#     # print(resultado)
#     return resultado
    
# print(sumar(2,4))
# valor=sumar(123,45)
# print("Segunda suma: ", valor)


def fun2(num1,num2):
    print("Hola desde funcion")
    suma=num1+num2
    resta=num1-num2
    return suma,resta

print(fun2(5,2))
res1,res2=fun2(33,298)
print(res1)
print(res2)