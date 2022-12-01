#1
hegy1 = float(input("Adja meg a hegy magasságát! "))
hegy2 = float(input("Adja meg a másik hegy magasságát! "))
if (hegy1 > hegy2):
    print(f"Hegy1 nagyobb mint hegy2")
elif(hegy2 > hegy1):
    print(f"Hegy2 nagyobb mint hegy1")
else:
    print(f"Egyenlőek!")
#2
def meter(menny):
    return menny/1000
def nagybetu(nev):
    nev = nev.upper()
    return nev
a = ["a","á","e","é","u","ú","ü","ű","o","ó","ö","ő","i","í"]
def nevelo(nev):
    for i in a:
        if (nev[0].lower() == i):
            return "Az"
    return "A"
nevek = []
magassag = []
for i in range(3):
    nevek.append(input(f"Adja meg a(z) {i+1}. hegymászó nevét! "))
    magassag.append(float(input(f"Adja meg a(z) {i+1}. hegymászó által megmászott hegy magasságát! ")))
    print(f"{nevek[i]} {meter(magassag[i]):0.2f}km magasra mászott")
    print(nagybetu(nevek[i]))
    print(f"{nevelo(nevek[i])} {nevek[i]}.")
