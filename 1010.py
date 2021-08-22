product1 = list(map(float, input().split(' ')))
product2 = list(map(float, input().split(' ')))
total = (product1[1] * product1[2]) + (product2[1] * product2[2])
print('VALOR A PAGAR: R$ %.2f' % total)