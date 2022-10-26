class ListaMusical:
    def __init__(self):
        self.temas={}
    #musiquita es el objeto que va a agregar al diccionario
    def add(self,musiquita):
        #Si se intenta ingresar un valor duplicado al diccionario salta excepcion
        if musiquita.codigo in self.temas:
            raise KeyError
        #Agrego objeto al diccionario    
        self.temas[ str(musiquita.codigo)] = musiquita
    #Donde musiquita es el objeto a remplazar y codigo es el id o key de lo que quiero reemplazar en el diccionario
    def update(self,musiquita,codigo):
        #Si se intenta actualizar un valor del diccionario que no existe salta excepcion
        if musiquita.codigo not in self.temas:
            raise KeyError
        #Actualizo el objeto que solicito el usuario    
        self.temas[ str(codigo)] = musiquita
    #codigo es el id o key del objeto del diccionario que quiero borrar
    def delete(self,codigo):
        #Si se intenta borrar una key de un objeto que no existe salta excepcion
        if codigo not in self.temas:
            raise KeyError
        self.temas.pop(str(codigo))
    #codigo es el id o key del objeto del diccionario que quiero buscar
    def find_by_id(self,codigo):
        #Si se intenta buscar una key de un objeto que no existe salta excepcion
        if codigo not in self.temas:
            raise KeyError
        return self.temas[str(codigo)]

    def find_all(self):
        listita=[]
        #recorro el diccionario y agrego cada uno como elemento a la lista que voy a retornar
        for i in self.temas:
            listita.append(self.temas[i])
        return listita 

class Error(Exception):
     """Base class for other exceptions"""
     pass

class KeyError(Error):
     pass