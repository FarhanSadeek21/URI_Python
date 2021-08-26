note_list = (100, 50, 20, 10, 5, 2, 1)
money = int(input())
print(money)
for i in range(7):
    count = money // note_list[i]
    print(str(count) + ' nota(s) de R$ ' + str(note_list[i]) +  ',00')
    money %= note_list[i]