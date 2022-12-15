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
    def nagybetu(self): #Nagybetűsre váltja a név első betűjét
        return (self.nev).capitalize()
    def vegzodes(self):
        return (self.nev).endswith("a") #Ha "a"-ra végződik akkor true lesz!
    def keres(self):
        return (self.nev).find("a") #Megkeresi benne az "a" betűt
    def szamok(self):
        return (self.foglalkozas).isalnum() #Igaz, ha minden karakter szám
    def betuk(self):
        return (self.nev).isalpha() #Igaz, ha minen karakter betű
    def kicsi(self):
        return (self.nev).islower() #Igaz, ha kisbetűs
    def nagy(self):
        return (self.nev).isupper() #Igaz, ha nagybetűs
    def add(self):
        return (self.nev).join("w") #Hozzá csatol egy "w" a névhez
    def nagybetus(self):
        return (self.nev).upper() #NAGYBETŰS
    def kisbetus(self):
        return (self.nev).lower() #kisbetűs
    def ls(self):
        return (self.nev).lstrip()
    def kicserel(self):
        return (self.nev).replace("o","ű") #kicseréli az "o" betűket "ű" betűre
    def rf(self):
        return (self.nev).rfind("k")  #Meg keresi az adott karaktert
    def rs(self):
        return (self.nev).rstrip()
hk = []
for i in range(3):
    nev = input("Add meg egy híres katona nevét! ")
    fog = input("Add meg a rangját! ")
    n = input("Add meg a nemzetiségét (o/n)! ")
    hk.append(Hires_katona(nev,fog,n))
for katona in hk:
    print(f"{katona.elotag()} {katona.nev} egy híres {katona.nemzetiseg}")
    print(f"{katona.nagybetu()} Végződése(a): {katona.vegzodes()} Hol van benne(a): {katona.keres()} Számok(foglalkozás): {katona.szamok()} Betűk(nev): {katona.betuk()}")
    print(f"Nagy: {katona.nagy()} Kicsi: {katona.kicsi()}, {katona.add()}, {katona.nagybetus()}, {katona.kisbetus()}")
    print(f"{katona.ls()} {katona.kicserel()} {katona.rf()} {katona.rs()}")
