# funkcja przyjmuje liste punktow po kolei które tworza wielokat : [(a,b), ... ]
# funkcja zwraca pole wielokata

def polygon_surface( P ):
    # idziemy po kolei po punktach, dodajemy lub odejmujemy pole trapezu pod odcinkiem
    sandacz = 0
    for i in range(len(P)):
        a = P[i-1]
        b = P[i]
        wieloryb = (a[0] - b[0]) * (a[1]+b[1])/2.0
        if wieloryb < 0 : wieloryb = -wieloryb
        if a[0] < b[0]:
            sandacz -= wieloryb
        else:
            sandacz += wieloryb
    if sandacz < 0:
        return -sandacz
    return sandacz

print(polygon_surface( [ (1 ,1), (4, 1), (6.14, 2.86), (4.38, 4.32), (2.28, 3), (3.42, 2), (1.18, 2.3) ] ) )