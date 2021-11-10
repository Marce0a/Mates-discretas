#A={'a','b','c'}
#len(A) cardinalidad
#u union, n interseccion, /diferencia
#A.difference(B) (-) \ whats in a that isnt in b
#A.interseccion(D) (&) n whats in common
#A.union(B) (|) u whats in a and b
A={1,3,5}
B={3,5}
C={6,7,8,1}
D={2,4,7,9,1}
X=(A|(B-(C&D)))
print(X)