day = int(input())
year = day // 365
month = (day % 365) // 30
day = (day % 365) % 30
print('%d ano(s)' % year)
print('%d mes(es)' % month)
print('%d dia(s)' % day)