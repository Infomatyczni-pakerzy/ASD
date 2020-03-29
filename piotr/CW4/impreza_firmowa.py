# szef nie moze z podwladnym
# wspolczynnik imprezowosci

class Employee:
    def __init__(self, fun, name):
        self.name = name
        self.emp = []
        self.fun = fun
        self.who = []   # who-list czyli kto wg tego zioma powinen isc
        self.f = -1
        self.g = -1


def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for vi in v.emp:
        x += g(vi)
    y = g(v)
    if x > y:
        v.f = x
        for vi in v.emp:
            for vj in vi.emp:   #adding who-list of double inferiors + v
                v.who.extend(vj.who)
        v.who.append(v)

    else:
        v.f = y
        for vi in v.emp:        #adding who-list of inferiors
            v.who.extend(vi.who)
    return v.f

def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for vi in v.emp:
        v.g += f(vi)
    return v.g

szef = Employee(12, "SZEFO")
pracownik1 = Employee(12, "Ja")
pracownik2 = Employee(3, "Debil")
sekretarka = Employee(8, "Baba")
sprzataczka = Employee(4, "Szmula")

sekretarka.emp.append(sprzataczka)
pracownik2.emp.append(sekretarka)
szef.emp = szef.emp + [pracownik1,pracownik2]

print(f(szef))
for someone in szef.who:
    print (someone.name)