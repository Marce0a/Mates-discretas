#.Tarea 3
#.Sucesión de Fibonacci
#f=[0, 1]
#while len(f)<17:
#    f.append(f[-1] + f[-2])
#len(f)
#print(f[-1])
#print(f)
#.Tarea 4
#.Solo se elimina el último número
#.Tarea 5
#.Tiempo de ejecución ¿Cuántas veces se evalúa 
#.la función de transición  durante la ejecución 
#.de la TM de la pregunta 4 con esa entrada específica
#.bits:1
#print(len("100010011")+4)
#-GRAFOS Y ÁRBOLES
#.Tarea 3
class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
u=6
v=2
conectar = [(1,2),(1,3),(2,4),(u,v),(3,5),(3,6),(4,6),(4,7),(5,8),(6,9),(7,9)]
mio = Grafo()
for (x,y) in conectar:
    mio.conecta(x,y)
#print(mio)
#print(mio.V)
#print(mio.vecinos)
#print(mio.E)
print(f'1: {max([ len(mio.vecinos[w]) for w in mio.V ])}')
size = len(mio.E) / 2
order = len(mio.V)
density = 2 * size / ( order * (order - 1 ))
print(f'2: {density}')

def floyd_warshall(G): 
    d = {}
    for v in G.V:
        d[(v, v)] = 0 # distancia reflexiva es cero
        for u in G.vecinos[v]: # para vecinos, la distancia es el peso
           d[(v, u)] = G.E[(v, u)]
    for intermedio in G.V:
        for desde in G.V:
            for hasta in G.V:
                di = None
                if (desde, intermedio) in d:
                    di = d[(desde, intermedio)]
                ih = None
                if (intermedio, hasta) in d:
                    ih = d[(intermedio, hasta)]
                if di is not None and ih is not None:
                    c = di + ih # largo del camino via "i"
                    if (desde, hasta) not in d or c < d[(desde, hasta)]:
                        d[(desde, hasta)] = c # mejora al camino actual
    return d
distances = floyd_warshall(mio)
print(f'3: {distances[(1, v)]}')
diameter = max(distances.values())
print(f'4: {diameter}')
forbidden = { u, v }
permitted = mio.V - forbidden
present = 0
for (x, y) in mio.E:
    if x in permitted and y in permitted:
        present += 1
present //= 2
print(f'5: {present}')