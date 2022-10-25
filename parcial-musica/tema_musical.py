
from logging import raiseExceptions

class TemaMusical: 
     def __init__(self,codigo=None,nombre=None,duracion=None,interprete=None): 
          self._codigo = codigo
          self._nombre = nombre
          self._duracion = duracion
          self._interprete = interprete
          
       
     # using property decorator 
     # a getter function 
     @property
     def codigo(self):  
         return self._codigo 

     @codigo.setter          
     def codigo(self, a): 
          if(a ==""): 
               raise EmptyError
          self._codigo = a    

     @property
     def nombre(self): 
         return self._nombre


     @nombre.setter          
     def nombre(self, a): 
          if(a ==""): 
               raise EmptyError
          self._nombre = a         

     @property
     def duracion(self):
          return self._duracion

     @duracion.setter
     def duracion(self, duracion):
          if (duracion== -1 ):
               raise EmptyError 
          self._duracion = duracion   

     @property
     def interprete(self):
          return self._interprete

     @interprete.setter
     def interprete(self, interprete):
          if (interprete==''):
               raise EmptyError 
          self._interprete=interprete   
     def __str__(self):
          a="codigo: "+str(self.codigo)+"\n\tnombre: "+str(self.nombre)+"\n\tduracion: "+str(self.duracion)+"\n\tinterprete: "+str(self.interprete)+"\n"
          return a
     def input(self,valor=None,codigo=None,nombre=None,duracion=None,interprete=None):
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

p1= TemaMusical()

#print(p1.__str__())



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