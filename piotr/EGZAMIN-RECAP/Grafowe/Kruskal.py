class Node_f_u:
    def __init__(self, idd):
        self.id = idd
        self.parent = self
        self.rank = 0

def find_f_u( V, x ):     # zwraca reprezentanta zbioru do ktorego nalezy x
    v = V[x]
    if v != v.parent:
        v.parent = find_f_u(V, v.parent.id)
    return v.parent

def union_f_u( V, x, y ):
    x = find_f_u(V, x)
    y = find_f_u(V, y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    
def insert_edge(E, i, e):   # E = [ (v, u, w), ...  ]   , v<u
    m = len(E)
    v = min(i, e[0])
    u = max(i, e[0])
    w = e[1]
    for j in range(m):
        if E[j] == (v, u, w):
            return
        if E[j][2] > w:
            E.insert(j, (v, u, w) )
            return
    E.append( (v, u, w) )

def Kruskal( G ):            # Graf G reprezentowany przez liste sasiedztwa i wag G = [ [...], ... ]
    n = len(G)
    E = []                   # Tablica z krawedziami
    A = []                   # Wynikowa tablica z krawedziami
    V = []                   # Tablica z wierzcholkami w strukturze find/union
    for e in G[0]:
        E.append( (0, e[0], e[1]) )
    E.sort( key=lambda item: item[2] )
    for i in range(1, n):    # Stworz posortowana tablice krawedzi (v, u, waga), gdzie v < u
        for e in G[i]:
            insert_edge(E, i, e)
    for i in range(n):
        V.append( Node_f_u(i) )
    
    for edge in E:           # jesli A + {edge} nie zawieraja cyklu dodaj egde do rozwiazania
        if find_f_u(V, edge[0]) != find_f_u(V, edge[1]):
            A.append( edge )
            union_f_u( V, edge[0], edge[1] )
    return A
    
    
    

G =[
        [ (1,2), (5,6), (6,1) ], # 0
        [ (0,2), (2,3) ],        # 1
        [ (1,3), (3,1), (6,2) ], # 2
        [ (2,1), (4,7) ],        # 3
        [ (3,7), (5,8), (6,5) ], # 4
        [ (0,6), (4,8) ],        # 5
        [ (0,1), (2,2), (4,5) ], # 6
   ]

print( Kruskal(G) )