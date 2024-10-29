liczba = int(input("Podaj liczbe: "))
suma = 0
while liczba != 0:
    ost = liczba%10
    print(ost)
    suma = suma + ost
    liczba = liczba//10
print(suma)