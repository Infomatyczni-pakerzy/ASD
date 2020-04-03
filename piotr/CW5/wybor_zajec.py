# problem wyboru zajęć - Piotr Zawiślan
# (b,a) - b-początek zajęć, a-koniec zajęć
# algorytm usuwa elementy tablicy, tak jak bylo na wykladzie, wiec skopiuję tablice
# tak by byla posortowana wzgledem indeksu [1]

def tasks(A):
    n_tasks = 0
    B = sorted(A, key = lambda tup: tup[1]) # wbudowana funkcja sortujaca względem [1] ( bylo napisane ze wolno uzywac )
    while( len(B) != 0):

        a = B[0][1]     # kiedy sie koncza się kończące się najwcześniej zajęcia
        n_tasks += 1
        del B[0]

        # Teraz przechodzimy po calej tablicy i usuwamy kolidujace elementy. Mozna by bylo przechodzic 
        # tylko po kawalku, ale trzeba by bylo skopiowac tablice jeszcze raz (dodatkowa poamiec) i posortowac 
        # wzgledem pierwszego elementu tupli. Wtedy breakujemy jezeli cos nie koliduje po raz pierwszy.

        length = len(B)
        i = 0
        while i < length:
            if B[i][0] < a : # <-jezeli zaczynaja sie przed a to usuwamy, bo musza się konczyc po a
                del B[i]
                length -= 1
            i += 1
    
    return n_tasks


# ma wyjsc 2
print( tasks( [(0,10), (10,20), (5,15)]) )
