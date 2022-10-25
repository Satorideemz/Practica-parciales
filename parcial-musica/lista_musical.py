class ListaMusical:
    def __init__(self):
        self.temas={}

    def add(self,musiquita):
        #if str(musiquita.codigo) == str(self.temas.get(str(musiquita.codigo))):
        #    raise KeyError
        if musiquita.codigo in self.temas:
            #todavia no la logro hacer funcar a la excepcion
            raise KeyError
        self.temas[ str(musiquita.codigo)] = musiquita

    def update(self,musiquita,codigo):
        self.temas[ str(codigo)] = musiquita
        #self.temas.update({'kJQP7kiw5Fk :'+musiquita})
    def delete(self,codigo):
        self.temas.pop(str(codigo))
    def find_by_id(self,codigo):
        return self.temas[str(codigo)]
    def find_all(self):
        listita=[]
        for i in self.temas:
            listita.append(self.temas[i])
        return listita 
class Error(Exception):
     """Base class for other exceptions"""
     pass

class KeyError(Error):
     pass
