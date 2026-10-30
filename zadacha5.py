tekst = input("Въведете текст: ")

pozicii = {}
for index, simvol in enumerate(tekst):
    if simvol not in pozicii:
        pozicii[simvol] = []
    pozicii[simvol].append(index)

for simvol, spisak in pozicii.items():
    print(f"{simvol}: {spisak}")