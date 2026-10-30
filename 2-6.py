n = int(input("Брой текстове: "))
search = input("Търсена дума: ")
new = input("Нова дума: ")

summary = 0

for i in range(1, n + 1):
    tekst = input("Текст " + str(i) + ": ")
    count = tekst.count(search)
    summary = summary + count
    tekst = tekst.replace(search, new)
    print("Брой срещания:", count)
    print("Резултат:", tekst)

print("Общ брой срещания:", summary)
