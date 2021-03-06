import random
"""Сортировка списка методом пузырька"""
l = [5, 5, 66, 76, 10, 0, 1, -4]  # Первое задание

for i in range(0, len(l)):
    for j in range(1, len(l) - i):
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
print(l)
"""Словарь цветов, в котором ключ - название или кодировка цвета;
значение - кортеж из rgb этого цвета"""
d = {'Пастельно-оранжевый': (255, 117, 20), 'Серый бетон': (104, 108, 94), 'Перламутровый медный': (118, 60, 40),
     'Фиолетовый': (139, 0, 255), 'Персидский синий': (102, 0, 255)}  # Второе задание
print(d)
"""
Заполняет два случайных набора чисел. Выводит оба набора. Указывает какие элементы:
входят одновременно в оба;
входят только в первое, но не входят во второе;
входят только во второе, но не входят в первое;
входят в первое или во второе, но не в оба из них одновременно.
"""
A = {random.randint(-100, 100) for i in range(10)}  # Третье задание
B = {random.randint(-100, 100) for i in range(10)}
print('a={} и b={}'.format(A, B))
print('A⋂B={}'.format(A.intersection(B)))
print('A\B={}'.format(A.difference(B)))
print('B\A={}'.format(B.difference(A)))
print('A^B={}'.format(A.union(B) - (A & B)))