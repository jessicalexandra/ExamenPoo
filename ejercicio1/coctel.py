class Coctel:
    def __init__(self):
        self.__nombre = None
        self.__precio = None
        self.__cantidadGradosAlcohol = None
        
    @property
    def nombre(self):    
        return self.__nombre
    
    @property
    def cantidadGradosAlcohol(self):    
        return self.__cantidadGradosAlcohol
    
    @property
    def precio(self):    
        return self.__precio
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @cantidadGradosAlcohol.setter
    def cantidadGradosAlcohol(self, cantidadGradosAlcohol):
        self.__cantidadGradosAlcohol = cantidadGradosAlcohol
        
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
       

class CoctelFrutas(Coctel):
    def __init__(self):
        self.__nivelFrescura=None
        
    @property
    def nivelFrescura(self):
        return self.__nivelFrescura
    
    @nivelFrescura.setter
    def precio(self,nivelFrescura):
        self.__nivelFrescura=nivelFrescura
        
    def costo(self,cantidad, nivelFrescura):
        if nivelFrescura==1:
            return cantidad*self.precio
        elif nivelFrescura==2:
            return (cantidad*self.precio)-(cantidad*self.precio*0.2)
        elif nivelFrescura==3:
            return (cantidad*self.precio)-(cantidad*self.precio*0.5)
        else:
            return "NO SE VENDE EL TRAGO"
        
class Shot(Coctel):
    
    def __init__(self):
        pass
        self.__temperatura = None
        
    @property
    def temperatura(self):    
        return self.__temperatura
        
    @temperatura.setter
    def temperatura(self, temperatura):
        self.__temperatura = temperatura
    
        
    def costo(self,cantidad):
        return self.precio*cantidad
    
    