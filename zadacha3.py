import random

n = int(input("Въведете n: "))

a = []
for i in range(n):
    a.append(random.randint(1, 9))

b = []
for i in range(0, n - 1, 2):
    b.append(a[i] + a[i + 1])

print("a =", a)
print("b =", b)
