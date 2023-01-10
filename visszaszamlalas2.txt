ora = int(input("Hány órás visszaszámlálást tervezünk? "))
hossza = ora
while ora > 0:
    print(f"Visszaszámlálás: {ora}")
    if (input("Fel kell függeszteni a visszaszámlálást (i/n)?") == "i"):
        hossza += 1
    ora -= 1
print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {hossza}")
