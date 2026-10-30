# Създаване на множество
s = set([1, 2, 3, 1])  # {1, 2, 3}
s2 = set("hello")  # {'h', 'e', 'l', 'o'}

# Обхождане на множество
for i in s2:
    print(i, end=' ')  # l h e o
print()

print(len(s2))  # 4

s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])

print(s | s1)  # {1, 2, 3, 4, 6} - обединение
print(s - s1)  # {1, 3} - разлика
print(s1 - s)  # {6}
print(s & s1)  # {2, 4} - пресичане
print(s ^ s1)  # {1, 3, 6} - симетрична разлика

# Други оператори
3 in s  # True
s == s1  # False
{1, 2} <= {1, 2, 3}  # True

# Методи на множествата
s1 = set([2, 4, 6])
s1.add(8)  # {2, 4, 6, 8}
s1.remove(8)  # {2, 4, 6}, грешка ако елемента го няма
s1.discard(100)  # няма грешка, въпреки че 100 го няма
x = s1.pop()
print("Премахнат елемент:", x)
print("Останали елементи:", s1)
s1.clear()  # set()


# ===== НИЗОВЕ =====

print('Hello, " World " ')  # Hello, " World "
print("hello", "world")  # hello world

# Многоредов текст
S = """ hello ,
*****
World!!! """

# Индекс и сечение
s1 = "Hello"
s1[0]  # 'H'
s1[:]  # 'Hello'
s1[:-1]  # 'Hell' - без последния символ
s1[1::2]  # 'el' - от втория символ, стъпка 2
s1[1:]  # 'ello' - без първия символ

"Hello" + "world"  # 'Helloworld'
"hell" in "Hello"  # False
"f" * 5  # 'fffff'

# Функции за работа с низове
len("Здравей")  # 7
str(123)  # '123'
print(repr("Hello World"))  # 'Hello World'

# Методи за работа с низове
"hello world".capitalize()  # 'Hello world'
", ".join(["apple", "banana", "cherry"])  # 'apple, banana, cherry'
"HeLLo".lower()  # 'hello'
"apple, banana, cherry".split(", ")  # ['apple', 'banana', 'cherry']
"   hello  \n".strip()  # 'hello'
"Hello World".swapcase()  # 'hELLO wORLD'
"hELLo worLD".title()  # 'Hello World'
"hello 123!".upper()  # 'HELLO 123!'

s = "banana"
print(s.find("an"))  # 1
print(s.find("x"))  # -1
s.index("an")  # 1, но s.index("x") връща ValueError

s = "hello world"
print(s.count("l"))  # 3

s = "one one one"
print(s.replace("one", "two"))  # two two two
print(s.replace("one", "two", 2))  # two two one (лимит 2)
