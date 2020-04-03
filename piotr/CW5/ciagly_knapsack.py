# ciagly problem plecakowy - Piotr Zawislan

# A = [(P1,W1)...], k - objetosc plecaka

def knapsack(A, k):
    B = []          # kopiujemy tablice tak aby zawierala tez wspolczynniki
    value = 0       # moglibysmy tez napisac np quickskorta do posortowania w miejscu,
                    # ale zakladam ze tablica A ma pozostac niezmieniona
    for i in range(len(A)):
        B.append((A[i][0], A[i][1], A[i][0]/A[i][1]))

    # wbudowana funkcja sortujaca odwrotnie względem wpolczynnika oplacalnosci
    B = sorted(B, key = lambda tup: tup[2], reverse=True)    

    for liquid in B:
        if liquid[1] > k:   #jezeli plyn nie zmiesci sie caly w plecaku
            value += ( liquid[2]*k )  # zwiekszamy wartosc o wartosc mozliwej do zabrania cieczy i zwracamy
            return value
        else:
            value += liquid[0]  # dodajemy caly plyn do naszego plecaka
            k -= liquid[1]      # zmniejszamy objetosc plecaka o objetosc zabranego plynu
    return value



#powinno wyjsc 12
print( knapsack( [(1,1), (10,2), (6,3) ] , 3) )
