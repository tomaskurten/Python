from cuenta import Cuenta
from banco import Banco

    
c1=Cuenta("Tomas")
c2=Cuenta("Ana")
# c1.__saldo=10000
# print(c1)
# print(c1.depositar(100))
# print(c1)

b1=Banco("Santa")
print(b1)
b1.agregar_cliente(c1)
b1.agregar_cliente(c2)
print(b1)