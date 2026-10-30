tekst = input("Въведете текст: ")

d = {}
for simvol in tekst:
    if simvol in d:
        d[simvol] = d[simvol] + 1
    else:
        d[simvol] = 1

print("Речникът се състои от", len(d), "елемента:")

keys = list(d.keys())
keys.sort()
for key in keys:
    print(f"{key}:{d[key]}")