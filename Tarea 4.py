#Tarea 4 y 5
#T4 num 3
#peso 7 y valor 12 a la instancia ¿cuánto vale el óptimo si el límite de peso de la mochila es 34?
peso_permitido = 34
objetos = ((5, 10), (8, 12), (4, 24), (12, 30), (5, 7), (2, 8), (1, 3))
peso_total = sum([objeto[0] for objeto in objetos])
valor_total = sum([objeto[1] for objeto in objetos])
if peso_total < peso_permitido: # cabe todo
    print('óptimo:', valor_total, 'con peso total de', peso_total)
else:
    cantidad = len(objetos)
    V = dict()
    for w in range(peso_permitido + 1):
        V[(w, 0)] = 0
    for i in range(cantidad):
        (peso, valor) = objetos[i]
        for w in range(peso_permitido + 1):
            cand = V.get((w - peso, i), -float('inf')) + valor
            V[(w, i + 1)] = max(V[(w, i)], cand)
    mejor_valor = max(V.values())
    peso_de_mejor = max(V.keys(), key = (lambda k: V[k]))[0]
    print('óptimo:', mejor_valor, 'con peso total de', peso_de_mejor)

#num4    
def camino(s, t, c, f): # construcción de un camino aumentante
    cola = [s]
    usados = set()
    camino = dict()
    while len(cola) > 0:
        u = cola.pop(0)
        usados.add(u)
        for (w, v) in c:
            if w == u and v not in cola and v not in usados:
                actual = f.get((u, v), 0)
                dif = c[(u, v)] - actual
                if dif > 0:
                    cola.append(v)
                    camino[v] = (u, dif)
    if t in usados:
        return camino
    else: # no se alcanzó
        return None

def ford_fulkerson(c, s, t): # algoritmo de Ford y Fulkerson
    if s == t:
        return 0
    maximo = 0
    f = dict()
    while True:
        aum = camino(s, t, c, f)
        if aum is None:
            break # ya no hay
        incr = min(aum.values(), key = (lambda k: k[1]))[1]
        u = t
        while u in aum:
            v = aum[u][0]
            actual = f.get((v, u), 0) # cero si no hay
            inverso = f.get((u, v), 0)
            f[(v, u)] = actual + incr
            f[(u, v)] = inverso - incr
            u = v
        maximo += incr
    return maximo
 
# datos tomados de:
# http://www.aduni.org/courses/algorithms/courseware/handouts/Reciation_09.html
c = {(0, 1): 16, (0, 2): 13, (1, 2): 10, (2, 1): 4, (3, 2): 9, \
(1, 3): 12, (2, 4): 14, (4, 3): 7, (3, 5): 20, (4, 5): 4, (2, 4): 9}
s = 1
t = 4
print(ford_fulkerson(c, s, t))
#
V=set()
for edge in c:
    (a, b)=edge
    V.add(a)
    V.add(b)
print(V)
highest=0
for s in V:
    for t in V - {s}:
        highest=max(highest, ford_fulkerson(c, s, t))
        print(highest)
#
for s in [0, 1, 2, 3, 4, 5]:
    for t in [0, 1, 2, 3, 4, 5]:
        print(ford_fulkerson(c, s, t))