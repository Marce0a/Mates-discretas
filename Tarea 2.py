#Tarea 2
#1 permutations
from math import factorial
factorial(5)
counter = 0
from itertools import permutations
stuff='abcdefg'
for ordering in permutations([x for x in stuff]):
    if ordering[0] == 'a' and ordering[-1] == 'f':
        print(ordering)
        counter += 1
        print(counter)
#2 combinations
def binom1(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
print(binom1(7,5))

def smartbinom(n,k):
    bigger=k if k>n-k else n-k
    smaller =k if k<n-k else n-k
    top=1
    for mult in range(bigger +1,n+1):
        top *= mult
    return top / factorial(smaller)
print(smartbinom(7,5))
