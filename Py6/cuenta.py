class Cuenta:

    # Constructor
    # Método especial
    def __init__(self, nom):
        # Atributos privados
        self.__titular= nom # Atributo de instancia
        self.__saldo= 0
    # Getters y Setters
    # decorador
    @property
    def saldo(self):
        return self.__saldo
    # getter
    @property
    def titular(self):
        return self.__titular   
    @titular.setter
    def titular(self, nom):
        self.__titular= nom   
    # Métodos de instancia
    def depositar(self, importe):
        estado= False


        if importe>0 and importe<1000:
            self.__saldo += importe
            estado= True
        return estado  
    def extraer(self, importe):
        estado= False
        if importe<=self.saldo:
            self.__saldo -= importe
            estado= True
        return estado


    def __str__(self):
        return f'Titular: {self.titular} Saldo actual: ${self.saldo}'
    
# c1=Cuenta("Tomas")
# c1.__saldo=10000
# print(c1)
# print(c1.depositar(10000))
# print(c1)