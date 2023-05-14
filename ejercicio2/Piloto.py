class Piloto:
    def __init__(self):
        self.__Nombre= None
        self.__fechaNacimiento= None
        self.__salarioAnual= None
        self.__Pais= None
    # _________________________________   
    @property
    def Nombre(self):
        return self.__Nombre
    
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @property
    def salarioAnual(self):
        return self.__salarioAnual
    @property
    def Pais(self):
        return self.__Pais
    
    #_______________________________________
    
    @Nombre.setter
    def Nombre(self,dato):
        self.__Nombre=dato

    @fechaNacimiento.setter
    def fechaNacimiento(self,dato):
        self.__fechaNacimiento=dato

    @salarioAnual.setter
    def salarioAnual(self,dato):
        self.__salarioAnual=dato

    @Pais.setter
    def Pais(self,dato):
        self.__Pais=dato