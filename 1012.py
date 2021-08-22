a, b, c = list(map(float, input().split(' ')))
triangle = 0.5 * a * c
print('TRIANGULO: %.3f' % triangle)
circle = 3.14159 * c * c
print('CIRCULO: %.3f' % circle)
trapezium = 0.5 * (a + b) * c
print('TRAPEZIO: %.3f' % trapezium)
square = b * b
print('QUADRADO: %.3f' % square)
rectangle = a * b
print('RETANGULO: %.3f' % rectangle)