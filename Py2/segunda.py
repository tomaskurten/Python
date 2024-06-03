# nota = -11
# if nota >= 0 and nota < 4:
#  print("Insuficiente.")
# elif nota >=4 and nota < 8:
#  print("En proceso.")
# elif nota==9:
#     print("muy bueno!!")
# elif nota==10:
#     print("Excelente")

# else:
#  print("Nota erronea")



# cont= 1
# suma= 0
# while cont <= 5:
#     num= int(input("Ingrese un número: "))
#     if num<0:
#         break
#     suma = suma + num
#     cont = cont + 1
# print("La suma es:", suma)
# print("El promedio es:", suma/cont)



suma= 0
for cont in range(5):
    num= int(input("Ingrese un número: "))
    suma = suma + num # Acumulamos, es equivalente suma += num
    if num<0:
        print("dentro del if")
        if suma>25:
            print("suma mayor a 25")    
print("La suma es:", suma)
print("El promedio es:", suma/(cont+1))


def funcion():
    print("")