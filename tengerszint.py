wr = open("H:\\tenger.txt","w")
def tengerszintek(h):
    if (h <= 200):
        return "alföld"
    elif (h >= 200 and h < 500):
        return "dombság"
    elif(h >= 500 and h < 1500):
        return "középhegység"
    elif(h >= 1500):
        return "magashegység"
helyek = []
magassagok = []
while True:
    hely = input("Adjon meg egy földrajzi hely nevét! ")
    wr.write(f"Adjon meg egy földrajzi hely nevét! {hely}\n")
    if (hely != ""):
        magassag = float(input("Adja meg a magasságát (m)! "))
        wr.write(f"Adja meg a magasságát (m)! {magassag}\n")
        helyek.append(hely)
        magassagok.append(magassag)
    else:
        break
for i in range(len(helyek)):
    print(f"{helyek[i]} ({magassagok[i]:0.0f}m) = {tengerszintek(magassagok[i])}")
    wr.write(f"{helyek[i]} ({magassagok[i]:0.0f}m) = {tengerszintek(magassagok[i])}\n")
wr.close()