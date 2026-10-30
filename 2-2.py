numbers = {2, 4, 6, 8}

f = int(input("Първо число: "))
s = int(input("Второ число: "))

numbers.add(f)
numbers.discard(s)

print("Крайно множество:", numbers)
