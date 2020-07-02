# 1. Wykonaj DFS usuwajac krawiedzie za sobą
# 2. Po przetworzeniu wierzcholka dodaj na poczatek cycklu
# 

class Node:
    def __init__(self, n):
        self.number = n
        self.processed = False
        self.adjacent = []

def delete_edge( u, v, W, S, R ):
    W[u].adjacent.remove(v)
    W[v].adjacent.remove(u)

def DFS_e( u, W, S, R ):
    # print(u.number, u.adjacent)
    S.append(u.number)
    if len(u.adjacent) == 0:
        u.processed = True
        S.pop()
        R.append(u.number)
        return
    for i in u.adjacent:
        delete_edge( u.number, i, W, S, R )
        DFS_e(W[i], W, S, R)

def find_Euler( G ):
    W = []
    R = []
    S = []
    for i in range(len(G)):
        W.append(Node(i))
        W[i].adjacent = G[i]
    DFS_e( W[0], W, S, R )
    R.reverse()
    R = S + R
    print(R)

G = [ 
      [1, 4],
      [0, 4],
      [4, 3],
      [2, 4],
      [0, 1, 2, 3]
    ]

G2 = [
        [1, 5],
        [0, 2, 5, 6],
        [1, 3, 4, 6],
        [2, 4],
        [2, 3, 5, 6],
        [0, 1, 4, 6],
        [1, 2, 4, 5]
     ]

find_Euler(G2)
