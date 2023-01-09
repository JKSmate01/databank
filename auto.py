import auto_alap as auto
autok = []
for _ in range(3):
    neve = input("Add meg egy autó márkanevét! ")
    ht = int(input("Add meg a henger térfogatát! "))
    orszag = input("Add meg a gyártó országát (j/n)! ")
    while (orszag != "j" and orszag != "n"):
        orszag = input("Add meg a gyártó országát (j/n)! ")
    autok.append(auto.Híres_auto(neve,ht,orszag))
for autokk in autok:
    print(f"{autokk.név} egy {autokk.nemzet()} autó {autokk.henger_térfogat} m3 henger térfogattal.")