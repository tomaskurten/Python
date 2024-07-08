# try:
#     num1=int(input("Ingrese numero: "))
#     num2=int(input("Ingrese numero: "))

#     resultado=num1/num2

#     print(resultado)
# except ZeroDivisionError:
#     print("Num 2 debe ser distinto de cero")
# except ValueError:
#     print("Los numeros deben ser enteros")
    
# print("Continuo con el programa...")


while True:
    try:
        num1=int(input("Ingrese numero: "))
        num2=3
        print(num2/num1)
        
    except:
        print("Ocurrio un error")
    else:
        print("Exito")
        break
    finally:
        print("Intento finalizado")

print("Fin del programa")