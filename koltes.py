kedd = int(input("Hány forintot költöttél kedden? "))
szerda = int(input("Hány forintot költöttél szerdán? "))
if (szerda > kedd):
    print(f"Szerdán költöttél többet, {szerda} Ft-ot.")
elif (kedd > szerda):
    print(f"Kedden költöttél többet, {kedd} Ft-ot.")
else:
    print(f"Kedden és szerdán is ugyanannyit költöttél.")
