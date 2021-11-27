import random

l = [5, 5, 66, 76, 10, 0, 1, -4]  # Первое задание

for i in range(0, len(l)):
    for j in range(1, len(l) - i):
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
print(l)

d = {'Пастельно-оранжевый': (255, 117, 20), 'Серый бетон': (104, 108, 94), 'Перламутровый медный': (118, 60, 40),
     'Фиолетовый': (139, 0, 255), 'Персидский синий': (102, 0, 255)}  # Второе задание
print(d)

A = {random.randint(-100, 100) for i in range(10)}  # Третье задание
B = {random.randint(-100, 100) for i in range(10)}
print('a={} и b={}'.format(A, B))
print('A⋂B={}'.format(A.intersection(B)))
print('A\B={}'.format(A.difference(B)))
print('B\A={}'.format(B.difference(A)))
print('A^B={}'.format(A.union(B) - (A & B)))