veg = 16
while True:
    ora = int(input("Hány óra van most? "))
    if (ora >= 8 and ora < veg):
        print("A bolt nyitva van.")
        print(f"Ennyi órád van még odaérni: {veg-ora}")
    else:
        print("A bolt zárva van.")