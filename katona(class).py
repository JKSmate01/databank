class Hires_katona:
    def __init__(self,nev,foglalkozas,nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if self.nemzetiseg == "n":
            return "Herr"
        else:
            return "Mister"
hk = []
for i in range(3):
    nev = input("Add meg egy híres katona nevét! ")
    fog = input("Add meg a rangját! ")
    n = input("Add meg a nemzetiségét (o/n)! ")
    hk.append(Hires_katona(nev,fog,n))
for katona in hk:
    print(f"{katona.elotag()} {katona.nev} egy híres {katona.nemzetiseg}")
