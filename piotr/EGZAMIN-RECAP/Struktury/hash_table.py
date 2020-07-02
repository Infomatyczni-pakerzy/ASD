class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        self.keep_looking = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)


def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N

def insert(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if hash_tab[idx].taken:
            idx = (idx + 1) % N
        else:
            break
    
    if not hash_tab[idx].taken:
        hash_tab[idx].key = key
        hash_tab[idx].taken = True


def find(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if not hash_tab[idx].taken: return None
        if hash_tab[idx].key == key: return idx
        idx = (idx + 1) % N
    
    return None

N=11
hash_tab = [Node() for i in range(N)]


test_keys = ['Jan', 'Anna', 'Piotr', 'Zofia', 'Witold', 'Irena', 'Marek', 'Monika']


for i in range(N):
    hash_tab[i].key = None
    hash_tab[i].taken = False

for k in test_keys:
    insert(hash_tab, k)

tab = [(str(hash_tab[i].key),
        str(hash_tab[i].taken),
        h(hash_tab[i].key) if hash_tab[i].taken else ' -'
       ) for i in range(N)]

print('Zawartosc tablicy:\t # key, taken, h(key)\n')
for e in tab:
    print('{:10}\t{:5}\t{:2}'.format(e[0], e[1], e[2]))
print('--------------------------')