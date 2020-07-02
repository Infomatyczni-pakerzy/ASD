 # Piotr Zawiślan
 #
 # Dany jest ciag klockow A = (K1, ..., Kn), K(i) := [a(i), b(i)]
 # wysokosc( K(i) ) = 1, obliczyc wysokosc konstrukcji
 #
 # Przepraszam za 100 linijek kodu, ale tak jakos wyszlo
 # Zlozonosc chyba O(nlogn), ale nie jestem pewien

import math

class Node:
    def __init__(self, i):
        self.index = i
        self.span = None
        self.leaf = False
        self.max_height = 0

    def parent_index(self):
        return (self.index-1)//2
    def left_index(self):
        return 2*self.index + 1
    def right_index(self):
        return 2*self.index + 2
 
def bricks( A ):           # rozwazam pozycje od 0 do najdalszej drugiej wspolrzednej klocka

    # IMPLPEMENTACJA DRZEWA
    farthest_brick = 0
    for brick in A:
        if farthest_brick < brick[1]:
            farthest_brick = brick[1]
    if farthest_brick%2 == 1:   farthest_brick += 1 # zamieniamy najdalsza pozycje na parzysta dla wygody
    B = []
    n = 2*farthest_brick - 1    # dlugosc tablicy reprezentujacej drzewo binarne
    for i in range(n):
        B.append( Node(i) )

    p = farthest_brick - 1
    for i in range(n-1, n//2 - 1, -1):  # dla lisci ustawiamy przedzialy bazowe
        B[i].span = (p, p+1)
        p -= 1
    for i in range(n//2 - 1, -1, -1):   # dla reszty wezlow obliczamy span()
        B[i].span = ( B[ B[i].left_index() ].span[0] , B[ B[i].right_index() ].span[1] )

    B[0].leaf = True
    B[0].max_height = 0
    # drzewo gotowe do dzialania algorytmu

    for brick in A:     # dla kazdego klocka po kolei wykonaj spadanie klocka
        level = check_level(B, brick, 0)    # oblicz wysokosc jaka bedzie gdy klocek spadnie
        place_brick(B, brick, level + 1, 0) # uloz klocek na szczycie

    return B[0].max_height


def check_level(B, brick, i):
    if i >= len(B)//2:  # jezeli B[i].span jest przedzialem bazowym
        return B[i].max_height
    left = B[i].span[0]
    right = B[i].span[1]
    center = (left+right)//2
    if B[i].leaf:   return B[i].max_height
    else:
        if brick[0] <= left and brick[1] >= right:      # jesli span w calosci zawiera sie w klocku
            return B[i].max_height
        elif brick[0] < center and brick[1] > center:   # jesli klocek rozciaga sie na lewo i prawo
            return max( check_level(B, brick, B[i].left_index()), check_level(B, brick, B[i].right_index()) )
        elif brick[1] <= center:       # jesli klocek jest po lewej
            return check_level(B, brick, B[i].left_index())
        elif brick[0] >= center:       # jesli klocek jest po prawej
            return check_level(B, brick, B[i].right_index())

def place_brick(B, brick, lvl, i):

    if i >= len(B)//2:  # jezeli B[i].span jest przedzialem bazowym
        B[i].max_height = lvl
        return

    left = B[i].span[0]
    right = B[i].span[1]
    center = (left+right)//2

    if brick[0] <= left and brick[1] >= right:   # jezeli przedzial sie zawiera w klocku - zwiekszamy 
        B[i].max_height = lvl

    elif brick[0] < center and brick[1] > center:   # klocek na srodku
        if B[i].leaf: 
            B[i].leaf = False
            B[ B[i].left_index() ].leaf = True
            B[ B[i].right_index() ].leaf = True
        place_brick(B, brick, lvl, B[i].left_index() )
        place_brick(B, brick, lvl, B[i].right_index() )

    elif brick[1] <= center:           # klocek po lewej
        if B[i].leaf:   
            B[i].leaf = False
            B[ B[i].left_index() ].leaf = True
        place_brick(B, brick, lvl, B[i].left_index() )

    elif brick[0] >= center:           # klocek po prawej
        if B[i].leaf: 
            B[i].leaf = False
            B[ B[i].right_index() ].leaf = True
        place_brick(B, brick, lvl, B[i].right_index() )

    if not B[i].leaf:   #po wykonaniu rekurencyjnych odwolan, dopasuj wysokosc w danym przedziale
        B[i].max_height = max ( B[ B[i].left_index() ].max_height, B[ B[i].right_index() ].max_height )

print( bricks( [ (1,3), (2,5), (0,3), (8,9), (4,6) ] ) )