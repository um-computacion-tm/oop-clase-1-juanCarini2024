class Persona:

    def __init__(self, nombre: str = "carlos", apellido: str = "messi", du: str = "45662458"):
        
        __atributo1__= 0
        
        self.__nombre__ = nombre
        
        self.__apellido__ = apellido
        
        self.__du__ = du

    def mostrar_datos(self):
    
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}')