from enum import Enum

class TipoEscenario(Enum):
    sanctum_sanctorum = [10000, 10, 10, 100]
    stark_tower = [20000, 20, 25, 200]
    xavier_school = [80000, 30, 40, 300]

class Escenarios(): 

    def __init__(self,x,y,a,b):
        self.__monedas = x
        self.__miermbros_ekip = y
        self.__movimientos = a
        self.__energia_vital = b
    
    def get_monedas(self): 
        return self.__monedas

    def get_miembros_ekip(self): 
        return self.__miermbros_ekip

    def get_movimientos(self): 
        return self.__movimientos

    def get_energia_vital(self): 
        return self.__energia_vital

    def from_str(x):

        escenario = x.lower()
        e = None

        for tp in TipoEscenario:
            if escenario == tp.name: 
                a = tp.value
                e = Escenarios(a[0], a[1], a[2], a[3])
                break
        
        if type(e) != Escenarios:
            raise TypeError("Invalid type for attribute nombre")

        return e
        
    #Son 3 escenarios preestablecidos que no se pueden cambiar

