'''Простенькие задачи:
Для начала в одном файле.
1) 5 примеров list comprehension
2) 5 examples with DICT comprehension
3) 5 примеров с set comprehensions'''

# Списки
l_1 = [a ** 2 for a in range(11)]
print(l_1)

l_2 = [a + a for a in range(5, 100) if a < 11]
print(l_2)

tel = ('+38050', '+38067', '+38066', '+38073', '+38099')
l_3 = [tel[a] + ' 000 00 00' for a in range(len(tel))]
print(l_3)

from random import randint

l_4 = [chr(randint(20, 200)) for a in range(10)]
print(l_4)

l_5 = [10, 20, 30, 40, 50]
l_6 = [l_5[a] ** 2 for a in range(len(l_5))]
print(l_6)

# словари
d_1 = {k: v for k, v in [('one', 'один'), ('two', 'два')]}
print(d_1)

buyings = [('bread', 1), ('milk', 2), ('water', 3)]
d_2 = {k: v for k, v in buyings}
print(d_2)

d_3 = {num: num ** 2 for num in range(1, 11)}
print(d_3)

d_4 = {i + 1: tel[i] + ' 111 11 11' for i in range(len(tel))}
print(d_4)

d_5 = {i + 1: chr(randint(20, 100)) for i in range(10)}
print(d_5)

# множества

s_1 = {a ** 2 for a in range(11)}
print(s_1)

s_2 = {randint(1, 5) for i in range(20)}
print(s_2)

s_3 = {i for i in range(20) if randint(0, 1) == 1}
print(s_3)

s_4 = {a for i in range(len(d_5)) for a in d_5.values()}
print(s_4)

s_5 = {a ** i for i in range(0, 4) for a in l_5}
print(s_5)
