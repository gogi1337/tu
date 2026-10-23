n = int(input("Въведете цяло число: "))

spisak = []
for i in range(1, n + 1):
    spisak.append(i)

obraten = spisak[::-1]

d = {}
for i in range(len(spisak)):
    d[spisak[i]] = obraten[i]

print("Списък:", spisak)
print("Речник:", d)
