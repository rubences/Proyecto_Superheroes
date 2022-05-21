from enum import Enum
from re import S
import string

class Organizacion: 
    def __init__(self, x, y):
        if type(x) != str:
            raise TypeError("Invalid type for attribute nombre")
        if type(y) != list:
            raise TypeError("Invalid type for attribute superheroes")
        if not y:
             raise ValueError("Invalid value for attribute superheroes")
        self.__nombre = x
        self.__superheroes= y

    def get_nombre(self): 
        return self.__nombre

    def get_superheroes(self): 
        return self.__superheroes

    def set_superheroes(self,x):
        self.__superheroes = x

    #Los nombres no se pueden cambiar, pero los superheroes pueden salir o entrar a distintas organizaciones, lo que es lógico. 

    def is_undefeated(self):
        x = False
        for i in range(len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                x = True
                break 
        return x

    def surrender(self): 
        for superheroe in self.__superheroes: 
            superheroe.die()

    def __str__(self): 
        tp = ""
        for superheroe in self.__superheroes: 
            tp += str(superheroe.get_identificador()) + ". Alias: " + superheroe.get_alias() + ", Tipo:" +  superheroe.get_tipo().name + ", Coste:" + str(superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n"

        return tp

    def __repr__(self):
        tr = ""
        for superheroe in self.__superheroes:
            tr += superheroe.get_identificador() + "\t" + superheroe.get_tipo() + "\t" + superheroe.get_movimientos() + "\n"

    def get_super_undefeated(self):
        sup_vivos = []
        for i in range(0, len(self.__superheroes)):
            if self.__superheroes[i].is_vivo():
                sup_vivos.append(self.__superheroes[i])

        return sup_vivos


    