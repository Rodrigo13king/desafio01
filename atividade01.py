hora1 = int(input("qual a hora do nascimento do seu filgo:    "))
minuto1 = int(input("qual o minuto:    "))
hora2 = int(input("qual a hora do nascimento do seu pai:    "))
minuto2 = int(input("qual o minuto:    "))


horageral = hora1 + hora2
minutogeral = minuto1 + minuto2

if minutogeral >= 60:
    horageral + horageral + 1
    minutogeral = minutogeral - 60
if horageral >= 12:
    horageral = horageral - 12
if horageral > 24:
    horageral = horageral - 24

print(horageral, minutogeral)