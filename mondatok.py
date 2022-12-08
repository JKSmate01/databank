import random as r
def nevelo(szo):
    mgn=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
    if (szo[0].lower() in mgn):
        return "Az"
    else:
        return "A"
def jelzo():
    return r.choice(["piros","nagy","könnyed"])
for i in range(3):
    szo = input(f"Adj meg egy szót({i+1}.)! ")
    print(f"{nevelo(szo)} {szo.lower()} {jelzo()}.")
