liczba = int(input("Podaj liczbe dodatnią: "))

i = 1
suma = 0

while  i <= liczba:
    suma =suma + i
    i += 1

wynik = "suma wszystkich liczb naturalnych niewiekszych nz {} wynosi {}"
wynik = wynik.format(liczba, suma)
print(wynik)