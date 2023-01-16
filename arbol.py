from collections import deque
class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.padre=None
        self.hijos=list()

    def __repr__(self):
        return str(self.valor)

class Arbol:
    def __init__ (self,nodo):
        self.raiz=nodo
    def es_ancestro(self,ancestro, descendiente):
        explorador=descendiente
        while True:
            if explorador is ancestro:
                return True
            if explorador is self.raiz:
                break
            explorador= explorador.padre
        return False
    def es_descendiente(self, descendiente, ancestro):
        return self.es_ancestro(ancestro,descendiente)
    
    def lista_ancestros(self,nodo):
        resultado=[]
        explorador=nodo
        while True:
            resultado.append(explorador)
            if explorador is  self.raiz:
                break
            explorador= explorador.padre
        return resultado
        

    
def padre_hijo (n1,n2):
    n1.hijos.append(n2)
    n2.padre=n1

def es_hoja(nodo):
        return not nodo.hijos

def es_hijo(hijo,padre):
    return hijo in padre.hijos

def es_padre(padre, hijo):
    return hijo.padre is padre

uno=Nodo(1)
dos = Nodo(2)
tres = Nodo(3)
cuatro = Nodo(4)
cinco = Nodo(5)
seis = Nodo(6)
siete = Nodo(7)
ocho = Nodo(8)
nueve = Nodo(9)
diez = Nodo(10)

padre_hijo(uno,dos)
padre_hijo(uno, tres)

padre_hijo(dos, cuatro)
padre_hijo(dos, cinco)
padre_hijo(dos, seis)

padre_hijo(cinco, nueve)
padre_hijo(nueve, diez)

padre_hijo(tres, siete)
padre_hijo(tres, ocho)

arbol=Arbol(uno)
arbol2= Arbol(dos)

##Prueba de ancestro
def DFS(nodo):
    lista = [nodo]
    for hijo in nodo.hijos:
        lista+= DFS(hijo)
    return lista

def BFS(nodo):
    solucion = []
    cola = deque([nodo])
    #while len(cola)!=0:
    while cola:
        actual = cola.pop()
        solucion.append(actual)
        for hijo in actual.hijos:
            cola.appendleft(hijo)
    return solucion
