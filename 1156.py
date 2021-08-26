total = 0
y = 1
for x in range(1, 40, 2):
    total += x / y
    y *=  2
print("%.2f" % total)