from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__Nombre=None
        self.__CasaMotor=None
        self.__PilotoPrincipal=Piloto()
        self.__Piloto2=Piloto()
        self.__costos=None

    @property
    def Nombre(self):
        return self.__Nombre
    @property
    def CasaMotor(self):
        return self.__CasaMotor

    @property
    def PilotoPrincipal(self):
        return self.__PilotoPrincipal
    @property
    def Piloto2(self):
        return self.__Piloto2
    @property
    def costos(self):
        return self.__costos
    #______________________________
    @Nombre.setter
    def Nombre(self,dato):
        self.__Nombre=dato

    @CasaMotor.setter
    def CasaMotor(self,dato):
        self.__CasaMotor=dato

    @PilotoPrincipal.setter
    def PilotoPrincipal(self,dato):
        self.__PilotoPrincipal=dato
    
    @Piloto2.setter
    def Piloto2(self,dato):
        self.__Piloto2=dato
    
    @costos.setter
    def costos(self,dato):
        self.__costos=dato
    
