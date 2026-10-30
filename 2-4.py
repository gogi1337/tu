w1 = input("Първа дума: ")
w2 = input("Втора дума: ")

w1l = set(w1.lower())
w2l = set(w2.lower())

print("Общи букви:", w1l & w2l)
