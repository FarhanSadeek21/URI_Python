user_input = input().split(' ')
code = float(user_input[0])
unit = float(user_input[1])
if code == 1:
     total = 4.00 * unit
     print('Total: R$ %.2f' % total)
elif code == 2:
    total = 4.50 * unit
    print('Total: R$ %.2f' % total)
elif code == 3:
    total = 5.00 * unit
    print('Total: R$ %.2f' % total)
elif code == 4:
    total = 2.00 * unit
    print('Total: R$ %.2f' % total)
elif code == 1:
    total = 1.50 * unit
    print('Total: R$ %.2f' % total)
    

'''
X,Y=list(map(int,input().split()))
if(X == 1):
    price  = (float) (4.00 * Y)
elif(X == 2):
    price  = (float) (4.50 * Y)
elif(X == 3):
    price  = (float) (5.00 * Y)
elif (X == 4):
    price  = (float) (2.00 * Y);
elif (X == 5):
    price  = (float) (1.50 * Y)
print("Total: R$ %.2f"%price)
'''