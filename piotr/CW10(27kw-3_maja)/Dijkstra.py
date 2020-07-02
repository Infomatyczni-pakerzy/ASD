# Piotr Zawiślan, nr indeksu: 400427
# Algorytm Dijkstry dla grafu skierowanego ( listy sasiedztwa + wag)

from queue import PriorityQueue     # bylo powiedziane na wykladzie, ze mozna
                                    # uzywam Q.empty(), Q.get() i Q.put()
class Node:
    def __init__(self, i, G):
        self.number = i
        self.visited = False
        self.parent = None
        self.d = float('inf')
        self.adjacent = G[i]

# zwraca tablice obliczonych pol parent ( z s do wszystkich wierzcholkow )
def dijkstra(G, s):
    n = len(G)
    N = []
    for i in range(n):
        N.append(Node(i, G))    # utworzenie tablicy wierzcholkow z atrybutami N
    
    Q = PriorityQueue()
    N[s].d = 0
    Q.put( (N[s].d, N[s].number) )   # wrzucamy s do kolejki priorytetowej,
    # na pozycji 1 jest N[s].number, bo PriorityQueue sortuje po 1 pozycji,
    # gdy na pozycji 0 są takie same liczby i to wywalalo exception

    while not Q.empty():
        ui = Q.get()[1]      # element o 1 indeksie z elementu w kolejce to numer danego wierzcholka
        u = N[ui]            # przypisanie atrybutow do numeru wierzcholka

        if N[u.number].visited == False:    # jezeli nie byl jeszcze przetworzony to przetworz (po to aby
            N[u.number].visited = True      #  nie trzeba bylo usuwac z kolejki wszystkich o danym numerze)
            for i in range( len(u.adjacent) ):
                Relax(u, i, N)
                Q.put( ( N[ u.adjacent[i][0] ].d , N[ u.adjacent[i][0] ].number ) )

    P = []
    for i in range(n):
        P.append( N[i].parent )
    return P


def Relax(u, i, N): # u - wierzcholek z ktorego wychodzimy, i - indeks wierzcholka do ktorego wchodzimy
    if N[ u.adjacent[i][0] ].d > u.d + u.adjacent[i][1]:   # N[ u.adjacent[i][0] ].d --> v.d
        N[ u.adjacent[i][0] ].d = u.d + u.adjacent[i][1]   # gdzie v --> odwiedzany wierzcholek
        N[ u.adjacent[i][0] ].parent = u.number


    
# TEST:
G = [ 
      [(1,0), (2,1)],
      [(3,1), (2,0)],
      [(3,0)],
      []
    ]
    
print( dijkstra( G, 0 ) )       # wypisze [None, 0, 1, 2]