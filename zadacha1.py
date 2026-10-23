chislo = input("Въведете цяло число: ")

if chislo[0] == "-":
    chislo = chislo[1:]

cifri = []
for c in chislo:
    cifri.append(int(c))

prav = tuple(cifri)
obraten = prav[::-1]

print("Цифри в прав ред:", prav)
print("Цифри в обратен ред:", obraten)
