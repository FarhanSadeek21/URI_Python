import math as m
x1, y1 = list(map(float, input().split(' ')))
x2, y2 = list(map(float, input().split(' ')))
distance = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print('%.4f' % distance)