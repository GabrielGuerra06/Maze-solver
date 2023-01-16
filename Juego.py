from arbol import *


nodos = dict()


# laberinto = [[0]*int(x)]*int(y)
busqueda = list()
laberinto= list()
inicio = tuple()
fin = tuple()
nodoAsignado = dict()
nodos = dict()
trazo = None
listaHijos = set()
lista_DFS = list()
lista_BFS = list()

def matriz():
    file = open(r"C:\Users\Gabri\OneDrive\Documentos\Universidad\E. de datos\Arboles\laberinto_1.in")
    coordenadas = file.readline().split()
    x,y = int(coordenadas[0]), int(coordenadas[1])
    global inicio 
    global fin
    global laberinto
    global busqueda
    for y, row in enumerate(file):
        contenido = list() 
        busqueda_contenido = list()
        for x, letra in enumerate(row[:-1]):
            contenido.append(row[x])
            busqueda_contenido.append((x,y))
            if letra == "A":
                inicio = inicio + (x,y)
            if letra == "B":
                fin = fin + (x,y)
        laberinto.append(contenido)
        busqueda.append(busqueda_contenido)
    file.close()


def asignarNodo():
    global busqueda
    global nodos
    global nodoAsignado
    for y, row in enumerate(busqueda):
        for x, cordenada in enumerate(row):
            nodos[f'{cordenada}'] = Nodo(cordenada)
            nodoAsignado[f'{cordenada}'] = laberinto[y][x]

def ruta():
    global trazo
    trazo = Arbol(nodos[(f'{inicio}')])

def relaciones(nodo):
    listaHijos.add(nodo)
    camino1 = nodos.get(f'{tuple(map(sum, zip(nodo.valor, (1,0))))}')
    camino2 = nodos.get(f'{tuple(map(sum, zip(nodo.valor, (-1,0))))}')
    camino3 = nodos.get(f'{tuple(map(sum, zip(nodo.valor, (0,1))))}')
    camino4 = nodos.get(f'{tuple(map(sum, zip(nodo.valor, (0,-1))))}')
    if f'{nodo}' in nodos: 
        if f'{camino1}' in nodos and nodoAsignado.get(f'{camino1}') != '0' and camino1 not in listaHijos:
            nodo.hijos.append(camino1)
            nodo.padre = camino1
            relaciones(camino1)
        if f'{camino2}' in nodos and nodoAsignado.get(f'{camino2}') != '0' and camino2 not in listaHijos:
            nodo.hijos.append(camino2)
            nodo.padre = camino2
            relaciones(camino2)
        if f'{camino3}' in nodos and nodoAsignado.get(f'{camino3}') != '0' and camino3 not in listaHijos:
            nodo.hijos.append(camino3)
            nodo.padre = camino3
            relaciones(camino3)
        if f'{camino4}' in nodos and nodoAsignado.get(f'{camino4}') != '0' and camino4 not in listaHijos:
            nodo.hijos.append(camino4)
            nodo.padre = camino4
            relaciones(camino4)


def recorrido1(trazo):
    global lista_DFS
    lista_pene = DFS(trazo.raiz)
    for i in lista_pene:
        lista_DFS.append(i.valor)
        if i.valor == fin:
            break
    return lista_DFS
    

    

def recorrido2(trazo):
    global lista_BFS
    lista_coito = BFS(trazo.raiz)
    for i in lista_coito:
        lista_BFS.append(i.valor)
        if i.valor == fin:
            break
    return lista_BFS

matriz()
asignarNodo()
ruta()
relaciones(nodos.get(f'{inicio}'))

print(recorrido1(trazo))

print(recorrido2(trazo))


