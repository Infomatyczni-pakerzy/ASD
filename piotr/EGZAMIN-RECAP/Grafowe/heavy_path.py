# algorytm dynamiczny:
# kazdy lisc ma najdluzsza sciezke rowna 0
# dla kazdego wezla obliczamy najdluzsza sciezke w jego poddrzewie
# jako max z najdluzszych sciezek kazdego dziecka badz max z sciezek 
# przechodzacych przez 2 poddrzewa

class Node:
    def __init__(self):
        self.id = ""
        self.children = 0       # liczba dzieci
        self.child = []         # lista par (dziecko, waga krawedzi)
        self.parent = None      # rodzic w drzewie
        self.high_path = None        # dlugosc najdluzszej sciezki w poddrzewie konczaca sie na tym wezle
        self.deep_path = None   # dlugosc najdluzszej sciezki w poddrzewie

def heavy_path( T ):        # T - korzen drzewa
    heavy_path_recursive( T )
    return T.deep_path

def heavy_path_recursive( N ):
    if N.children == 0:
        N.high_path = 0
        N.deep_path = 0
    else:
        max_deep = 0
        max_shallow_1 = 0
        max_shallow_2 = 0
        for kid in N.child:
            heavy_path_recursive(kid[0])
            if max_deep < kid[0].deep_path: max_deep = kid[0].deep_path
            if max_shallow_1 < kid[0].high_path + kid[1]:
                max_shallow_2 = max_shallow_1
                max_shallow_1 = kid[0].high_path + kid[1]
            elif max_shallow_2 < kid[0].high_path + kid[1]:
                max_shallow_2 = kid[0].high_path + kid[1]
        N.high_path = max_shallow_1
        N.deep_path = max( max_shallow_1 + max_shallow_2, max_deep )

def print_tree_attributes( T ):
    print(T.id, T.deep_path, T.high_path, sep = "   ")
    if T.children == 0:
        return
    for c in T.child:
        print_tree_attributes(c[0])

#A = Node()
#B = Node()
#C = Node()
#A.children = 2
#A.child = [ (B, 5), (C, -1) ]

A = Node()
A.id = "A"

B = Node()
B.id = "B"

C = Node()
C.id = "C"

D = Node()
D.id = "D"

E = Node()
E.id = "E"

F = Node()
F.id = "F"

G = Node()
G.id = "G"

H = Node()
H.id = "H"

I = Node()
I.id = "I"

A.children = 2
A.child = [ (B,5), (C,-1) ]
B.children = 3
B.child = [ (D,4), (E,-3) ,(F,2)]
C.children = 2
C.child = [ (H,7), (I,2) ]
E.children = 1
E.child = [ (G,2) ]


print( heavy_path(A) )
print_tree_attributes(A)