def foros(amount):
    for ember in range(amount):
        nev = input("Add meg a beteg nevét! ")
        th = float(input(f"Mennyi {nev} testhőmérséklete? "))
        while th < 34 or th > 45:
            print(f"Ez nem reális hőfok! ({th})")
            th = float(input(f"Mennyi {nev} testhőmérséklete? "))
        print(nev)
        if (th < 36):
            print("Enyhe kihülés.")
        elif (th  >= 36 and th  < 37):
            print("Normál!")
        elif (th  >= 37 and th  <= 38):
            print("Hő emelkedés!")
        elif (th  > 38 and th  < 40):
            print("Magas láz!")
        elif (th  > 40):
            print("Kórház!")
def listas(amount):
    hofokok = []
    nevek = []
    for _ in range(amount):
        nev = input("Add meg a beteg nevét! ")
        th = float(input(f"Mennyi {nev} testhőmérséklete? "))
        while th < 34 or th > 45:
            print(f"Ez nem reális hőfok! ({th})")
            th = float(input(f"Mennyi {nev} testhőmérséklete? "))
        hofokok.append(th)
        nevek.append(nev)
    for i in range(len(hofokok)):
        print(nevek[i])
        if (hofokok[i] < 36):
            print("Enyhe kihülés.")
        elif (hofokok[i] >= 36 and hofokok[i] < 37):
            print("Normál!")
        elif (hofokok[i] >= 37 and hofokok[i] <= 38):
            print("Hő emelkedés!")
        elif (hofokok[i] > 38 and hofokok[i] <= 40):
            print("Magas láz!")
        elif (hofokok[i] > 40):
            print("Kórház!")
    hofokok.sort()
    for i in range(len(hofokok)):
        print(hofokok[i],end=",")
    print("")
    hofokok.reverse()
    for i in range(len(hofokok)):
        print(hofokok[i],end=",")
    print("")
am = int(input("Hány embert akarsz megvizsgálni? "))
w = int(input("foros:0 listas:1? "))
if (w == 0):
    foros(am)
elif(w==1):
    listas(am)
