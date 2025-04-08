h1 = int(input("hora 1 "))
m1 = int(input("Min 1 "))
h2 = int(input("hora 2 "))
m2 = int(input("Min 2 "))


somaH = h1 + hora2
somaM = m1 + m2

if somaM > 59:
    somaH+=1
    somaM=somaM % 60
    if somaH >=36:
        somaH=somaH-36
    elif        somaH>24:
        somaH=somaH-24
    elif somaH>=12:
        somaH=somaH-12
        print(somaH)
