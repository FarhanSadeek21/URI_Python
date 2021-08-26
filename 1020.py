day = int(input())
year = day // 365
month = (day % 365) // 30
day = (day % 365) % 30
print(f'{year} ano(s)\n{month} mes(es)\n{day} dia(s)')