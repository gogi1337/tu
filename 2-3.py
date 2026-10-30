text = input("Въведете текст: ")

stripped = text.strip()

print("Почистен текст:", stripped)
print("Главни букви:", stripped.upper())
print("Малки букви:", stripped.lower())
print("Брой символи:", len(stripped))
