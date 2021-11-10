#Tarea 5
#T5 P1
start=3
finish=53
step=5
a=[x for x in range(start, finish, step)]
print(a)
print(15 in a)
#
def bbinaria(ordenados, buscado):
    n = len(ordenados)
    print('Tengo', ordenados, 'y busco por', buscado)
    if n == 0: # no hay nada
        return False
    pos = n // 2 # div. entera
    pivote = ordenados[pos]
    if pivote == buscado:
        return True # encontrado
    elif buscado < pivote: # viene antes del pivote
        return bbinaria(ordenados[: pos], buscado)
    else: # pivote < buscado # viene desp. del pivote
        return bbinaria(ordenados[pos + 1 :], buscado)

print(bbinaria([x for x in range(3, 53, 5)], 15))

#desde = 3
#hasta = 53
#paso = 5
#ubicar = 15
#print(bbinaria([x for x in range(desde, hasta + 1, paso)], ubicar))

#T5 P2
n=43
from math import log
from math import ceil, floor
log(n,2)
print(floor(log(n,2))+1)

from math import log, floor
old = 0
for n in range(1, 101):
    h = floor(log(n, 2)) + 1
    if h != old:
        print(n, h)
    old = h

#T5 P3
from arbol import Arbol
a = Arbol()
for clave in (97, 66, 67, 42, 79, 24, 89, 90, 59, 6):
    a.agrega(clave)

def ubicar(nodo, buscado):
    print('buscando por', buscado, 'en', nodo.contenido)
    if nodo.contenido==buscado:
        return True
    if buscado < nodo.contenido and nodo.izquierdo is not None:
        return ubicar(nodo.izquierdo, buscado)
    if buscado > nodo.contenido and nodo.derecho is not None:
        return ubicar(nodo.derecho, buscado)
    return False

print(ubicar(a.raiz, 36))

#T5 P4
def editdist(p, q, ce = 1, ci = 1, cr = 1): #ce-costo eliminacion, cinsercion, creemplazo
    d= dict()
    np= len(p) + 1
    nq= len(q) + 1
    for i in range(np):
        d[(i, 0)] = i * ci #mov horizontal es insertar
    for j in range(nq):
        d[(0, j)] = j * ce #mov vertical es eliminar
    for i in range(1, np):
        for j in range(1, nq):
            eli = d[(i - 1, j)] + ce
            ins = d[(i, j - 1)] + ci
            #movimiento diagonal es reemplazar
            ree = d[(i - 1, j - 1)] + cr * (p[i - 1] != q[j - 1])
            d[(i, j)] = min(eli, ins, ree)
    return d[(np - 1, nq - 1)]
print(editdist('sabado', 'domingo', 3, 1, 3)) #elim, ins, reemp

#T5 P5
grafo = {(3, 4): 4, (1, 3): 4, (2, 3): 2, (2, 4): 1, (3, 4): 2, (4, 6): 1, (5, 6): 2}
 
from copy import deepcopy
cand = deepcopy(grafo)
arbol = set()
peso = 0
comp = dict()
 
while len(cand) > 0:
    arista = min(cand.keys(), key = (lambda k: cand[k]))
    del cand[arista] # se consideran una sola vez
    (u, v) = arista
    c = comp.get(v, {v})
    if u not in c:
        arbol.add(arista)
        peso += grafo[arista]
        nuevo = c.union(comp.get(u, {u}))
        for w in nuevo:
            comp[w] = nuevo    
 
print('MST con peso', peso, ':', arbol)
