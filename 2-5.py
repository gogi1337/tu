sent = input("Въведете изречение: ")

words = sent.split()

print("Брой думи:", len(words))

for word in words:
    if len(word) == 1:
        print(word, "–", len(word), "символ")
    else:
        print(word, "–", len(word), "символа")

result = "-".join(words)
print("Резултат:", result)
