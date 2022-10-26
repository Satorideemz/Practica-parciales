
from logging import raiseExceptions

class TemaMusical:
     #Defino constructor de clase, None indica que es opcional para el objeto 
     def __init__(self,codigo=None,nombre=None,duracion=None,interprete=None): 
          self._codigo = codigo
          self._nombre = nombre
          self._duracion = duracion
          self._interprete = interprete
       
     #getters y setters
     #En los mismos pongo un raise exception que me indica cuando el usuario intenta ingresar un valor no valido
     @property
     def codigo(self):  
         return self._codigo 
     #Excepcion para codigo vacio
     @codigo.setter          
     def codigo(self, a): 
          if(a ==""): 
               raise EmptyError
          self._codigo = a    
     
     @property
     def nombre(self): 
         return self._nombre

     #Excepcion para nombre vacio
     @nombre.setter          
     def nombre(self, a): 
          if(a ==""): 
               raise EmptyError
          self._nombre = a         

     @property
     def duracion(self):
          return self._duracion
     #Excepcion para duracion negativa
     @duracion.setter
     def duracion(self, duracion):
          if (duracion== -1 ):
               raise ValueError 
          self._duracion = duracion   
     
     @property
     def interprete(self):
          return self._interprete
     #Excepcion para interprete vacio

     @interprete.setter
     def interprete(self, interprete):
          if (interprete==''):
               raise EmptyError 
          self._interprete=interprete

     #Aca sobre-escribo el metodo __str__ para que cumpla con el formato que demanda el test
     def __str__(self):
          a="codigo: "+str(self.codigo)+"\n\tnombre: "+str(self.nombre)+"\n\tduracion: "+str(self.duracion)+"\n\tinterprete: "+str(self.interprete)+"\n"
          return a
     #Defino metodo que pide el test, es donde el usuario ingresa los datos por teclado y crea el objeto
     def input(self,valor=None,codigo=None,nombre=None,duracion=None,interprete=None):
          #Si recibe como parametro un True, entonces no pide el atributo codigo, pasa a ser opcional
          if valor== False or valor==None: 
               self.codigo=str(input("escriba el codigo"))
          self.nombre=str(input("escriba el nombre"))
          self.duracion=str(input("escriba la duracion"))
          self.interprete=str(input("escriba el interprete"))
                
class Error(Exception):
     """Base class for other exceptions"""
     pass

class EmptyError(Error):
     pass
class ValueError(Error):
     pass


# class Geeks: 
#      def __init__(self): 
#           self._age = 0
       
#      # using property decorator 
#      # a getter function 
#      @property
#      def age(self): 
#          print("getter method called") 
#          return self._age 
       
#      # a setter function 
#      @age.setter 
#      def age(self, a): 
#          if(a < 18): 
#             raise ValueError("Sorry you age is below eligibility criteria") 
#          print("setter method called") 
#          self._age = a 